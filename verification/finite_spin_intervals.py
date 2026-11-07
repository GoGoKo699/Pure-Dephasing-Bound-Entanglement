"""Generic finite-spin moments and state-dependent witnesses in rational intervals.

Uses shared rational interval arithmetic. Physical parameters may be intervals;
all subsequent calculations preserve outward rounding.
"""
from fractions import Fraction as F
from pathlib import Path
import sys,json
import sympy as S

BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE))
from independent_dephasing_certificate import I,expminus,cos,sin

def iexpminus(x):
    x=I.as_i(x);assert 0<=x.lo<=x.hi
    scale=1
    while x.hi/scale>=1:scale*=2
    y=I(expminus(x.hi/scale).lo,expminus(x.lo/scale).hi)
    return y**scale

def icos(x):
    x=I.as_i(x)
    far=max(abs(x.lo),abs(x.hi));near=F(0) if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi))
    assert far<1
    return I(cos(far).lo,cos(near).hi)

def isin(x):
    x=I.as_i(x);assert -1<x.lo<=x.hi<1
    return I(sin(x.lo).lo,sin(x.hi).hi)

def imat(M):return [[I.as_i(x) for x in row] for row in M]

def mmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),I(0)) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):return list(map(list,zip(*A)))

def spin_moments(m,R,B,t):
    R=imat(R);B=imat(B);t=I.as_i(t);n=len(R)
    a=[]
    for j in range(n):
        z=iexpminus(t*R[j][j]/m)
        for k in range(n):z=z*icos(t*B[j][k]/m)**m
        a.append(z)
    V=[[I(int(i==j and i<n)) for j in range(2*n)] for i in range(2*n)]
    for j in range(n):
        for k in range(n):
            angle=t*B[k][j]/m
            z=m*a[k]*isin(angle)/icos(angle)
            V[j][n+k]=V[n+k][j]=z
        g=iexpminus(4*t*R[j][j]/m)
        for k in range(n):g=g*icos(2*t*B[j][k]/m)**m
        V[n+j][n+j]=1+F(m-1,2)*(1-g)
    for j in range(n):
        for k in range(j+1,n):
            gs=[]
            for sign in [-1,1]:
                g=iexpminus(t*(R[j][j]+R[k][k]+2*sign*R[j][k])/m)*icos(t*B[j][k]/m)**(2*(m-1))
                for l in range(n):
                    if l not in [j,k]:g=g*icos(t*(B[j][l]+sign*B[k][l])/m)**m
                gs.append(g)
            V[n+j][n+k]=V[n+k][n+j]=F(m,2)*(gs[0]-gs[1])
    return a,V

def score(W,V):return sum((W[j][k]*V[k][j] for j in range(len(W)) for k in range(len(W))),I(0))

def two_mode_bound(W,a,na=2):
    n=len(a);assert n==4 and na==2
    bounds=[]
    for inds,js in [([0,1,4,5],[0,1]),([2,3,6,7],[2,3])]:
        w=[[W[j][k] for k in inds] for j in inds]
        om=[[I(0) for k in range(4)] for j in range(4)]
        om[0][2]=a[js[0]];om[1][3]=a[js[1]];om[2][0]=-a[js[0]];om[3][1]=-a[js[1]]
        ow=mmul(om,w);ow2=mmul(ow,ow)
        ss=-sum((ow2[j][j] for j in range(4)),I(0))/2
        det=F(str(S.Matrix(w).det()))
        bounds.append(2*(ss+2*a[js[0]]*a[js[1]]*I(det).sqrt()).sqrt())
    return sum(bounds,I(0))

def ww_data():
    G=S.Matrix([[2,0,0,0,1,0,0,0],[0,1,0,0,0,0,0,-1],[0,0,2,0,0,0,-1,0],[0,0,0,1,0,-1,0,0],[1,0,0,0,2,0,0,0],[0,0,0,-1,0,4,0,0],[0,0,-1,0,0,0,2,0],[0,-1,0,0,0,0,0,4]])
    J=S.Matrix([[0,1],[-1,0]]);Om=S.diag(J,J,J,J)
    N=S.zeros(4,8);N[0,0]=2;N[0,4]=-1;N[1,2]=2;N[1,6]=1;N[2,1]=3;N[2,7]=1;N[3,3]=3;N[3,5]=1
    W=N.T*N;delta=S.Rational(1,30);t=S.Rational(30)
    R=G+delta*S.eye(8);B=-Om
    # Carrier witness A^T W A with A=(-tB,I)/sqrt(2t); square root cancels.
    M=(-t*B).row_join(S.eye(8));Wc=M.T*W*M/(2*t)
    frac=lambda A:[[F(str(z)) for z in row] for row in A.tolist()]
    return frac(R),frac(B),frac(W),frac(Wc),F(t)

def certify_ww(m):
    R,B,W,Wc,t=ww_data();a,V=spin_moments(m,R,B,t)
    val=score(Wc,V)
    c=[(a[2*k]+a[2*k+1])/2 for k in range(4)]
    bound=12*(c[0]+c[1])+2*(c[2]+c[3]);gap=bound-val
    return {'m':m,'physical_qubits':8*m,'t':str(t),'delta':'1/30','witness_score':val.record(),'separable_bound':bound.record(),'strict_gap':gap.record(),'certified_entangled':gap.lo>0}

def main():
    result={'construction':'Werner-Wolf integer covariance transduction, delta=1/30, t=30','finite_spin':[]}
    for m in [4096,8192,16384,32768,65536]:
        r=certify_ww(m);result['finite_spin'].append(r)
        print(json.dumps({'m':m,'physical_qubits':8*m,'score':r['witness_score']['display'],'bound':r['separable_bound']['display'],'gap':r['strict_gap']['display'],'certified':r['certified_entangled']}),flush=True)
        if r['certified_entangled']:break
    (BASE/'finite_spin_ww_certificate.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
