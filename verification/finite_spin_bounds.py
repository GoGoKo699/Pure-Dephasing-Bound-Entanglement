"""Non-asymptotic rational bounds for collective-spin dephasing transfer.

These sufficient bounds are deliberately conservative. They do not replace the
sharper exact-moment interval certificates for a specified finite example.
"""
from fractions import Fraction as F
from pathlib import Path
import json

BASE=Path(__file__).resolve().parent

def transfer_error_bound(R,B,W,t,m,na):
    n=len(R);x=[[t*z for z in row] for row in B]
    xmax=max(abs(z) for row in x for z in row)
    assert m>=1 and F(m)>=4*xmax
    u=[sum(z*z for z in row) for row in x]
    v=[sum(z**4 for z in row) for row in x]
    A=[t*R[j][j]+u[j]/2 for j in range(n)]
    eta=[min(F(1),A[j]/m+v[j]/(8*m**3)) for j in range(n)]
    qp=[[abs(x[k][j])*eta[k]+abs(x[k][j])**3/(2*m**2) for k in range(n)] for j in range(n)]
    pp=[[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        d=4*A[j];z=d/m+2*v[j]/m**3
        pp[j][j]=d/(2*m)+v[j]/m**2+F(m,4)*z*z
    for j in range(n):
        for k in range(j+1,n):
            hs=[];ws=[]
            for sign in [-1,1]:
                terms=[x[j][l]+sign*x[k][l] for l in range(n) if l not in [j,k]]
                hs.append(t*(R[j][j]+R[k][k]+2*sign*R[j][k])+x[j][k]**2+sum(z*z for z in terms)/2)
                ws.append(2*x[j][k]**4+sum(z**4 for z in terms))
            zs=[h/m+w/(8*m**3) for h,w in zip(hs,ws)]
            pp[j][k]=pp[k][j]=sum(ws)/(16*m**2)+F(m,4)*sum(z*z for z in zs)
    score=sum(2*abs(W[j][n+k])*qp[j][k] for j in range(n) for k in range(n))
    score+=sum(abs(W[n+j][n+k])*pp[j][k] for j in range(n) for k in range(n))
    threshold=F(0)
    for inds in [list(range(na)),list(range(na,n))]:
        threshold+=sum(W[j][j]+W[n+j][n+j] for j in inds)*max(eta[j] for j in inds)
    return {'covariance_score_error':score,'threshold_loss':threshold,'total':score+threshold,'magnetization_errors':eta}

def sufficient_m(R,B,W,t,na,gap):
    xmax=max(abs(t*z) for row in B for z in row)
    m=1
    while m<max(F(1),4*xmax):m*=2
    attempts=[]
    while True:
        e=transfer_error_bound(R,B,W,t,m,na)
        attempts.append({'m':m,'error_upper':str(e['total']),'display':float(e['total'])})
        if e['total']<gap:
            return {'m':m,'qubits':len(R)*m,'certified_gap_lower':str(gap-e['total']),'display_gap_lower':float(gap-e['total']),'attempts':attempts}
        m*=2

def main():
    data=json.loads((BASE/'gaussian_exact_certificate.json').read_text())
    R=[[F(z,1000) for z in row] for row in data['R_integer_1000']]
    B=[[F(z,1000) for z in row] for row in data['B_integer_1000']]
    W=[[F(z,100000) for z in row] for row in data['W_integer_100000']]
    result=sufficient_m(R,B,W,F(28,5),2,F(data['margin_rational_lower_bound']))
    result['purpose']='Conservative general transfer theorem, not optimized example size; separate exact-moment certificate proves m=512.'
    dest=BASE/'finite_spin_bound_results.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['m','qubits','display_gap_lower','purpose']},indent=2))

if __name__=='__main__':main()
