"""Exact rational and outward-rounded interval checks for the dephasing witness.

Consumes the coarsened public matrices in gaussian_exact_certificate.json.
No floating-point comparisons are used to decide positivity or witness violation.
The trigonometric/exponential intervals use alternating Taylor bounds at |x|<1.
"""
if not __debug__:
    raise RuntimeError("Run this exact certificate without Python optimization (-O).")

from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json
import sympy as S

BASE=Path(__file__).resolve().parent
DEN=10**50

def down(x):
    x=F(x)
    return F((x.numerator*DEN)//x.denominator,DEN)

def up(x):
    x=F(x)
    return -down(-x)

class I:
    def __init__(self,lo,hi=None):
        self.lo=down(lo);self.hi=up(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def as_i(x):return x if isinstance(x,I) else I(x)
    def __add__(self,b):
        b=I.as_i(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I.as_i(b)
    def __rsub__(self,b):return I.as_i(b)+-self
    def __mul__(self,b):
        b=I.as_i(b);v=[x*y for x in [self.lo,self.hi] for y in [b.lo,b.hi]]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.as_i(b);assert b.lo*b.hi>0
        return self*I(1/b.hi,1/b.lo)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        ans=I(1);b=self
        while n:
            if n&1:ans=ans*b
            n//=2
            if n:b=b*b
        return ans
    def sqrt(self):
        assert self.lo>=0
        a=isqrt((self.lo.numerator*DEN**2)//self.lo.denominator)
        b=isqrt((self.hi.numerator*DEN**2)//self.hi.denominator)+1
        return I(F(a,DEN),F(b,DEN))
    def record(self):return {'lower':str(self.lo),'upper':str(self.hi),'display':[float(self.lo),float(self.hi)]}

def expminus(x):
    x=F(x);assert 0<=x<1
    even=sum(((-x)**k)/factorial(k) for k in range(41))
    odd=even-x**41/factorial(41)
    return I(odd,even)

def cos(x):
    x=abs(F(x));assert x<1
    even=sum((-1)**k*x**(2*k)/factorial(2*k) for k in range(41))
    odd=even-x**82/factorial(82)
    return I(odd,even)

def sin(x):
    x=F(x)
    if x<0:return -sin(-x)
    assert x<1
    even=sum((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(41))
    odd=even-x**83/factorial(83)
    return I(odd,even)

def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),I(0)) for j in range(len(b[0]))] for i in range(len(a))]

def exact_minors(M):return [S.factor(M[:k,:k].det()) for k in range(1,M.rows+1)]

def finite_spin(m,R,B,W,t):
    a=[]
    for j in range(4):
        v=expminus(t*R[j][j]/m)
        for k in range(4):v=v*cos(t*B[j][k]/m)**m
        a.append(v)
    V=[[I(int(i==j and i<4)) for j in range(8)] for i in range(8)]
    for j in range(4):
        for k in range(4):
            v=m*a[k]*sin(t*B[k][j]/m)/cos(t*B[k][j]/m)
            V[j][k+4]=V[k+4][j]=v
        g=expminus(4*t*R[j][j]/m)
        for k in range(4):g=g*cos(2*t*B[j][k]/m)**m
        V[j+4][j+4]=1+F(m-1,2)*(1-g)
    for j in range(4):
        for k in range(j+1,4):
            gs=[]
            for sign in [-1,1]:
                g=expminus(t*(R[j][j]+R[k][k]+2*sign*R[j][k])/m)*cos(t*B[j][k]/m)**(2*(m-1))
                for l in range(4):
                    if l not in [j,k]:g=g*cos(t*(B[j][l]+sign*B[k][l])/m)**m
                gs.append(g)
            V[j+4][k+4]=V[k+4][j+4]=F(m,2)*(gs[0]-gs[1])
    score=sum((W[i][j]*V[j][i] for i in range(8) for j in range(8)),I(0))
    bounds=[]
    for inds,js in [([0,1,4,5],[0,1]),([2,3,6,7],[2,3])]:
        w=[[W[i][j] for j in inds] for i in inds]
        om=[[I(0) for j in range(4)] for i in range(4)]
        om[0][2]=a[js[0]];om[1][3]=a[js[1]];om[2][0]=-a[js[0]];om[3][1]=-a[js[1]]
        ow=mul(om,w);ow2=mul(ow,ow)
        ss=-sum((ow2[i][i] for i in range(4)),I(0))/2
        dd=F(str(S.Matrix(w).det()))
        rootdet=I(dd).sqrt()
        bounds.append(2*(ss+2*a[js[0]]*a[js[1]]*rootdet).sqrt())
    total=sum(bounds,I(0));gap=total-score
    assert gap.lo>0
    return {'m':m,'physical_qubits':4*m,'magnetizations':[v.record() for v in a],'witness_score':score.record(),'separable_lower':total.record(),'strict_gap':gap.record(),'certified':True}

def main():
    data=json.loads((BASE/'gaussian_exact_certificate.json').read_text())
    R=S.Matrix(data['R_integer_1000'])/1000;B=S.Matrix(data['B_integer_1000'])/1000;W=S.Matrix(data['W_integer_100000'])/100000
    C=R+S.I*B;CT=C.copy();CT[:2,:2]=C[:2,:2].T;CT[:2,2:]=-R[:2,2:];CT[2:,:2]=-R[2:,:2]
    minors={}
    for name,M in [('C',C),('C_partial_transpose',CT),('W',W)]:
        ds=exact_minors(M);assert all(d>0 for d in ds);minors[name]=[str(d) for d in ds]
    t=S.Rational(28,5);V=S.eye(4).row_join(-t*B).col_join((t*B).row_join(S.eye(4)+2*t*R-t*t*B*B))
    score=S.trace(W*V);assert score==S.Rational(data['TrWV'])
    om=S.zeros(4);om[:2,2:]=S.eye(2);om[2:,:2]=-S.eye(2)
    lowers=[]
    for inds,ell in zip(([0,1,4,5],[2,3,6,7]),data['local_trace_rational_lower_bounds']):
        w=W.extract(inds,inds);ss=-S.trace((om*w)**2)/2;dd=w.det();ell=S.Rational(ell)
        # 2 sqrt(s+2sqrt(d))>ell, checked by squaring only positive quantities.
        z=(ell**2/4-ss)/2
        assert z<0 or z*z<dd
        lowers.append(ell)
    assert sum(lowers)>score
    as_f=lambda M:[[F(str(z)) for z in row] for row in M.tolist()]
    result={'source':'gaussian_exact_certificate.json','checks_use_floating_point':False,'exact_positive_leading_principal_minors':minors,'gaussian_witness_score':str(score),'gaussian_separable_rational_lower':str(sum(lowers)),'gaussian_gap_rational_lower':str(sum(lowers)-score),'finite_spin':[finite_spin(m,as_f(R),as_f(B),as_f(W),F(28,5)) for m in [512,1024]],'precision_denominator':str(DEN)}
    dest=BASE/'independent_dephasing_certificate.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'gaussian_gap_lower':float(sum(lowers)-score),'finite_spin':[{k:r[k] for k in ['m','physical_qubits','certified']}|{'gap':r['strict_gap']['display']} for r in result['finite_spin']],'file':str(dest)},indent=2))

if __name__=='__main__':main()
