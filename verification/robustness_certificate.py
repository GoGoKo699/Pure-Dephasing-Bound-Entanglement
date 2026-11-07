"""Finite-spin parameter robustness via exact interval enclosures."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as S
from finite_spin_intervals import I,spin_moments,score,two_mode_bound

BASE=Path(__file__).resolve().parent

def main():
    data=json.loads((BASE/'gaussian_exact_certificate.json').read_text())
    R=[[F(z,1000) for z in row] for row in data['R_integer_1000']]
    B=[[F(z,1000) for z in row] for row in data['B_integer_1000']]
    W=[[F(z,100000) for z in row] for row in data['W_integer_100000']]
    C=S.Matrix(R)+S.I*S.Matrix(B);CT=C.copy();CT[:2,:2]=C[:2,:2].T;CT[:2,2:]=-S.Matrix(R)[:2,2:];CT[2:,:2]=-S.Matrix(R)[2:,:2]
    shifted={}
    for name,M,shift in [('C',C,S.Rational(1,500)),('CT',CT,S.Rational(1,250))]:
        Q=M-shift*S.eye(4);ds=[S.factor(Q[:k,:k].det()) for k in range(1,5)]
        assert all(z>0 for z in ds)
        shifted[name]={'strict_eigenvalue_lower':str(shift),'positive_leading_minors':[str(z) for z in ds]}
    result={'m':512,'physical_qubits':2048,'fixed_time':'28/5','shifted_exact_positivity':shifted,'cases':[]}
    cases=[('coefficient_box',F(1,100000)),('coefficient_box',F(1,10000)),('additional_diagonal_dephasing',F(1,1000)),('additional_diagonal_dephasing',F(1,200))]
    for kind,eps in cases:
        rr=[[I(z) for z in row] for row in R];bb=[[I(z) for z in row] for row in B]
        if kind=='coefficient_box':
            for j in range(4):
                for k in range(j,4):rr[j][k]=rr[k][j]=I(R[j][k]-eps,R[j][k]+eps)
                for k in range(j+1,4):bb[j][k]=I(B[j][k]-eps,B[j][k]+eps);bb[k][j]=-bb[j][k]
            # Frobenius norm bound: ||Delta C|| <= sqrt(28) eps < 6 eps,
            # and ||Delta CT|| <= 2 ||Delta C|| < 12 eps.
            assert 6*eps<F(1,500) and 12*eps<F(1,250)
        else:
            for j in range(4):rr[j][j]=I(R[j][j],R[j][j]+eps)
            # Positive diagonal addition preserves C and CT positivity exactly.
        a,V=spin_moments(512,rr,bb,F(28,5));v=score(W,V);b=two_mode_bound(W,a);g=b-v
        rec={'kind':kind,'radius_or_upper':str(eps),'witness_score':v.record(),'separable_lower':b.record(),'gap':g.record(),'certified_all_parameters':g.lo>0,'all_time_PPT_preserved':True}
        result['cases'].append(rec)
        print(json.dumps({'kind':kind,'epsilon':str(eps),'score':v.record()['display'],'bound':b.record()['display'],'gap':g.record()['display'],'certified':g.lo>0}),flush=True)
    (BASE/'robustness_certificate.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
