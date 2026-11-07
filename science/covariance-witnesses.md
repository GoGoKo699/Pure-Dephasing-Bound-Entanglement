# Covariance witnesses for arbitrary separable states

[Scientific route](README.md) · [Dephasing model](model.md)

The entanglement test must apply to every separable state in the physical Hilbert space. Restricting the alternatives to Gaussian states, or replacing a spin commutator by a canonical one, would not establish the finite-qubit result. The following inequality avoids both restrictions.

## Local covariance constraints

Use real observable vectors $r_A,r_B$, finite second moments and doubled covariances as in [the model](model.md). Their mean commutator matrices are defined by

$$
(\Omega_X)_{jk}=-i\langle[r_{X,j},r_{X,k}]\rangle,\qquad X\in\{A,B\}.
$$

Each $\Omega_X$ is real antisymmetric. The Robertson constraint is $V_X+i\Omega_X\succeq0$. For a separable mixture, the full covariance is

$$
V=\sum_\ell p_\ell(V_{A,\ell}\oplus V_{B,\ell})+2\operatorname{Cov}_\ell(\mu_{A,\ell}\oplus\mu_{B,\ell}).
$$

The last term is positive semidefinite. Moreover, averaging the local uncertainty constraints gives $\overline V_X+i\Omega_X\succeq0$, because the mean commutator is linear in the state. No assumption is made about entanglement among subsystems belonging to the same party.

## The witness bound

For a real positive semidefinite weight $W$, let $W_A,W_B$ be its principal local blocks, in the chosen observable ordering. Then every separable state obeys

$$
\operatorname{Tr}(WV)\geq f(W_A,\Omega_A)+f(W_B,\Omega_B),
\qquad
f(M,\Omega)=\operatorname{Tr}\left|i\sqrt M\,\Omega\sqrt M\right|.
$$

**Proof.** Positivity of $W$ lets us discard the positive covariance of the local means. It remains to bound each $\operatorname{Tr}(M\overline V)$. First suppose $M>0$, and set $Z=\sqrt M\,\overline V\sqrt M$ and $K=\sqrt M\,\Omega\sqrt M$. The uncertainty constraint and its complex conjugate give $Z+iK\succeq0$ and $Z-iK\succeq0$. If $P_+$ and $P_-$ are the positive and negative spectral projectors of $iK$, use $\operatorname{Tr}[P_+(Z-iK)]\geq0$ and $\operatorname{Tr}[P_-(Z+iK)]\geq0$. Adding these inequalities yields $\operatorname{Tr}Z\geq\operatorname{Tr}|iK|$; the possible zero eigenspace contributes a nonnegative term. Equality in this covariance optimization is attained at $Z=|iK|$, which is real symmetric and satisfies the constraint. The semidefinite witness bound follows by replacing $M$ by $M+\epsilon I$ and taking $\epsilon\downarrow0$; for singular $M$, the corresponding infimum need not be attained. $\square$

For canonical oscillator coordinates, this is the familiar local symplectic bound underlying [Gaussian covariance separability](../references/RELATED_WORK.md#gaussian-covariances-and-reservoir-transfer). Its necessity holds for non-Gaussian separable states as well.

## A two-mode formula

For a positive four-by-four local block $M$ and a real nonsingular four-by-four commutator matrix $\Omega$, define

$$
s=-\frac12\operatorname{Tr}[(\Omega M)^2],\qquad d=\det(M)\det(\Omega).
$$

The eigenvalues of $i\sqrt M\,\Omega\sqrt M$ occur as two opposite pairs, and therefore

$$
f(M,\Omega)=2\sqrt{s+2\sqrt d}.
$$

The formula extends continuously when a commutator weight vanishes. It reduces witness verification to two scalar radicals. For the rational four-mode example, positivity and these radicals are bounded by exact integer arithmetic and rational squaring inequalities.

## Collective spins require their actual commutators

For group $j$ containing $m$ qubits, set

$$
Q_j=\frac{\sum_{a=1}^{m}Z_{ja}}{\sqrt{2m}},\qquad
P_j=-\frac{\sum_{a=1}^{m}Y_{ja}}{\sqrt{2m}},\qquad
\overline X_j=\frac1m\sum_{a=1}^{m}X_{ja}.
$$

The exact commutator is $[Q_j,P_k]=i\delta_{jk}\overline X_j$. For a party consisting of two groups, use

$$
\Omega_X(a)=\begin{pmatrix}0&\operatorname{diag}(a_j,a_k)\\-\operatorname{diag}(a_j,a_k)&0\end{pmatrix},\qquad a_j=\langle\overline X_j\rangle.
$$

These magnetizations belong to the evolved state. They are not set to one. Their linearity under mixing is exactly what makes the separable bound valid for every finite-spin state. The left side and threshold are both measured or calculated from the same state. This is a state-dependent separability criterion, with exact finite-size evaluation described in [the transfer theorem](finite-spin-transfer.md).

## Sparse variance witnesses

Sometimes the weight matrix is best specified as a sum of outer products of a few real vectors. Then its score is a sum of doubled variances, and positivity is immediate. The [integer-covariance construction](reservoir-embedding.md#an-explicit-integer-example) uses such a witness: its separable lower bound follows directly from local canonical uncertainty relations. This simpler example explains the mechanism, while the denser four-mode certificate supplies a smaller explicit finite-qubit construction.
