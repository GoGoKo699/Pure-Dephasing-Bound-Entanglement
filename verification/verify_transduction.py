"""Exact algebra checks for the pure-dephasing Gaussian transduction theorem.

No optimization or floating-point positivity decisions are used. Run with Python
and SymPy. The target ordering is (q1,p1,q2,p2,q3,p3,q4,p4); carrier ordering
is (Q1,...,Q8,P1,...,P8). Alice owns target modes 1,2 and carriers 1,...,4.
"""

if not __debug__:
    raise RuntimeError("Run this exact certificate without Python optimization (-O).")

import json
from pathlib import Path
import sympy as s


def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


J = s.Matrix([[0, 1], [-1, 0]])
Omega = s.diag(J, J, J, J)
Omega_pt = s.diag(-J, -J, J, J)
n = 8
I = s.eye(n)
O = s.zeros(n)
Jc = O.row_join(I).col_join((-I).row_join(O))
D = s.diag(1, -1, 1, -1, 1, -1, 1, -1)
S = s.diag(-1, -1, -1, -1, 1, 1, 1, 1)
B = -Omega

G0 = s.Matrix([
    [2, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, -1],
    [0, 0, 2, 0, 0, 0, -1, 0],
    [0, 0, 0, 1, 0, -1, 0, 0],
    [1, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, -1, 0, 4, 0, 0],
    [0, 0, -1, 0, 0, 0, 2, 0],
    [0, -1, 0, 0, 0, 0, 0, 4],
])
F = s.Matrix([
    [2, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 3, 0, 1, 0, 0],
])
W = F.T * F

t = s.symbols("t", positive=True)
delta = s.symbols("delta", nonnegative=True)
G = G0 + delta * I
C = G - s.I * Omega
Ct = C.copy()
Ct[:4, :4] = C[:4, :4].T
Ct[:4, 4:] = -G[:4, 4:]
Ct[4:, :4] = -G[4:, :4]
assert zero(S * Ct * S - (G - s.I * Omega_pt))

# Vacuum-output covariance and the explicitly local symplectic completion.
V = I.row_join(-t * B).col_join((t * B).row_join(I + 2*t*G - t*t*B*B))
Kx = (-t * B).row_join(I)
Ky = (D * t * B).row_join(D)
K = Kx.col_join(Ky)
assert zero(K * Jc * K.T - 2*t*s.diag(Omega, Omega))
assert zero(Kx * V * Kx.T / (2*t) - (G + I/(2*t)))
assert zero(Kx * Jc * Ky.T)
assert zero(Ky * V * Ky.T / (2*t) - D*(G + I/(2*t) + 2*t*I)*D)
assert zero(Kx * V * Ky.T / (2*t) - (G + I/(2*t))*D)

# Exact dilation output: carrier drift plus target-reservoir quadratures.
A = I.row_join(O).col_join((t*B).row_join(I))
N = s.zeros(n).col_join(s.sqrt(2*t)*I)
assert zero(A * Jc * A.T + N * Omega * N.T - Jc)
assert zero(A * A.T + N * G * N.T - V)
assert zero(Kx * A / s.sqrt(2*t) - O.row_join(I/s.sqrt(2*t)))
assert zero(Kx * N / s.sqrt(2*t) - I)

# Independent squeezed carrier inputs: extraction adds s_in/(2t) identity.
s_in = s.symbols("s_in", positive=True)
Vin = s.diag(I/s_in, s_in*I)
Vout = A * Vin * A.T + N * G * N.T
assert zero(Kx * Vout * Kx.T/(2*t) - G - s_in*I/(2*t))

# WW uncertainty and PPT uncertainty have the same exactly known spectrum.
x = s.symbols("x")
char_expected = x**2 * (x-3)**2 * (x*x-6*x+6)**2
assert s.expand((G0+s.I*Omega).charpoly(x).as_expr()-char_expected) == 0
assert s.expand((G0+s.I*Omega_pt).charpoly(x).as_expr()-char_expected) == 0

# Positivity of W is certified constructively by W=F^T F.
assert s.trace(W * G0) == 26
assert s.trace(W) == 30
assert W[:4, :4] == s.diag(4, 9, 4, 9)
assert W[4:, 4:] == s.eye(4)
sep_bound = s.Integer(28)
score = s.simplify(s.trace(W * (G + I/(2*t))))
assert score == 26 + 30*delta + 15/t

benchmark = {delta: s.Rational(1, 30), t: s.Integer(30)}
C_bench = C.subs(benchmark)
Ct_bench = Ct.subs(benchmark)
minors_c = [s.factor(C_bench[:k, :k].det()) for k in range(1, n+1)]
minors_ct = [s.factor(Ct_bench[:k, :k].det()) for k in range(1, n+1)]
assert all(q.is_positive is True for q in minors_c + minors_ct)
assert score.subs(benchmark) == s.Rational(55, 2)
assert sep_bound-score.subs(benchmark) == s.Rational(1, 2)

result = {
    "status": "all exact identities and inequalities passed",
    "target_order": "q1,p1,q2,p2,q3,p3,q4,p4",
    "carrier_order": "Q1,...,Q8,P1,...,P8",
    "target_bipartition": "modes 1,2 | modes 3,4",
    "carrier_bipartition": "modes 1,...,4 | modes 5,...,8",
    "WW_uncertainty_characteristic_polynomial": str(s.factor(char_expected)),
    "WW_uncertainty_eigenvalues_each_twice": ["0", "3", "3-sqrt(3)", "3+sqrt(3)"],
    "target_WW_covariance": [list(map(int, row)) for row in G0.tolist()],
    "witness_factor_F": [list(map(int, row)) for row in F.tolist()],
    "witness_target_score": "26",
    "witness_trace": "30",
    "separable_lower_bound": "28",
    "decoded_witness_score": str(score),
    "sufficient_entanglement_region": "delta >= 0 and delta + 1/(2*t) < 1/15",
    "benchmark_delta": "1/30",
    "benchmark_time": "30",
    "benchmark_score": "55/2",
    "benchmark_violation": "1/2",
    "benchmark_C_leading_principal_minors": list(map(str, minors_c)),
    "benchmark_CT_leading_principal_minors": list(map(str, minors_ct)),
}
out = Path(__file__).with_name("transduction_verification.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
