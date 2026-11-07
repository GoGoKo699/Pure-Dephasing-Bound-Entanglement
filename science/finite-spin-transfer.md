# Finite-spin transfer of strict dephasing witnesses

[Scientific route](README.md) · [Covariance witnesses](covariance-witnesses.md) · [Explicit 2,048-qubit example](four-mode-certificate.md)

A strict covariance-witness violation for the vacuum oscillator dynamics survives in a sufficiently large, finite collection of individually polarized qubits. This page proves that statement with explicit error bounds. The convergence is of the moments and witness; no trace-norm or diamond-norm convergence of changing Hilbert spaces is asserted.

## 1. Statement of the transfer theorem

Fix a finite number $`n`$ of groups and a bipartition of their indices into $`A`$ and $`B`$. Let

```math
C=R+iB_0\succeq0,
\qquad R=R^T\in\mathbb R^{n\times n},
\qquad B_0=-B_0^T\in\mathbb R^{n\times n}.
```

The subscript on $`B_0`$ distinguishes this real antisymmetric matrix from party $`B`$. Define

```math
C^{\Gamma}=
\begin{pmatrix}
R_{AA}-i(B_0)_{AA}&-R_{AB}\\
-R_{BA}&R_{BB}+i(B_0)_{BB}
\end{pmatrix}.
```

Assume $`C^\Gamma\succeq0`$. At each positive integer $`m`$, place $`m`$ qubits in each group and set

```math
Q_j^{(m)}=\frac{\sum_{\alpha=1}^m Z_{j\alpha}}{\sqrt{2m}},
\qquad
P_j^{(m)}=-\frac{\sum_{\alpha=1}^m Y_{j\alpha}}{\sqrt{2m}},
\qquad
\overline X_j^{(m)}=\frac1m\sum_{\alpha=1}^m X_{j\alpha}.
```

Use the generator

```math
\mathcal L_m(\rho)=
\sum_{j,k=1}^n C_{jk}
\left(
Q_j^{(m)}\rho Q_k^{(m)}
-\frac12\{Q_j^{(m)}Q_k^{(m)},\rho\}
\right)
```

and initial state

```math
\rho_m(0)=|+\rangle\langle+|^{\otimes nm}.
```

Every $`\mathcal L_m`$ is a bounded finite-dimensional Lindblad generator. The coefficient matrix does not change with $`m`$; the normalization of the collective observables is explicit.

Let $`V_\infty(t)`$ be the doubled covariance of the corresponding product-vacuum oscillator evolution,

```math
V_\infty(t)=
\begin{pmatrix}
I&-tB_0\\
tB_0&I+2tR-t^2B_0^2
\end{pmatrix},
```

in the order $`(Q_1,\ldots,Q_n,P_1,\ldots,P_n)`$. For a real positive semidefinite matrix $`W`$, let $`W_A,W_B`$ be its principal submatrices on each party's local quadratures. With the canonical local symplectic forms $`\Omega_A,\Omega_B`$, write

```math
b_\infty(W)=
\sum_{X=A,B}
\mathrm{Tr}\left|
i\sqrt{W_X}\Omega_X\sqrt{W_X}
\right|.
```

**Finite-spin transfer theorem.** If, for some fixed finite $`t>0`$ and $`W\succeq0`$,

```math
\Delta=b_\infty(W)-\mathrm{Tr}[W V_\infty(t)]>0,
```

then there is a finite integer $`m_*`$ such that for every $`m\ge m_*`$, the state $`\rho_m(t)`$ is entangled across the selected cut. It is PPT across that cut at every nonnegative time. The bounds in Section 5 give a computable sufficient choice of $`m_*`$.

The same conclusion holds whenever a certified positive lower bound for $`\Delta`$ is available. Strict positivity of $`C`$, $`C^\Gamma`$, or $`W`$ is not required for the theorem. Positive definiteness is useful for parameter robustness and exact finite examples.

## 2. Physicality and PPT are uniform in the group size

The bounded observables commute and are real in the computational basis. The positivity conditions in the theorem are independent of m. Applying [Proposition 1 in the dephasing model](model.md#a-sufficient-all-time-ppt-condition) to these observables proves complete positivity and PPT preservation for every group size and every nonnegative time. The Hamiltonian introduced by transposition belongs only to the conjugated description. Every computational-basis population remains fixed.

## 3. Exact finite-spin moments

Define the doubled centered covariance by

```math
(V_m)_{ab}=
\langle\{r_a-\langle r_a\rangle,r_b-\langle r_b\rangle\}\rangle,
\qquad
r=(Q_1^{(m)},\ldots,Q_n^{(m)},P_1^{(m)},\ldots,P_n^{(m)}).
```

All first moments vanish. The initial state and channel are invariant under simultaneous reversal of every $`Z`$ coordinate, which also reverses every $`P_j^{(m)}`$.

For compactness set

```math
x_{jk}=t(B_0)_{jk},\qquad r_{jk}=tR_{jk},\qquad
a_j=\langle\overline X_j^{(m)}\rangle.
```

The exact formulas, valid for every positive integer $`m`$, are

```math
a_j=
e^{-r_{jj}/m}\prod_{\ell=1}^n
\cos(x_{j\ell}/m)^m,
\tag{1}
```

```math
(V_m)_{QQ}=I,
\qquad
(V_m)_{Q_jP_k}
=m a_k\tan(x_{kj}/m),
\tag{2}
```

where the product form $`m e^{-r_{kk}/m}\sin(x_{kj}/m) \cos(x_{kj}/m)^{m-1}\prod_{\ell\ne j}\cos(x_{k\ell}/m)^m`$
defines the same expression at any zero of the displayed denominator.

For diagonal momentum entries,

```math
(V_m)_{P_jP_j}=
1+\frac{m-1}{2}
\left[
1-e^{-4r_{jj}/m}
\prod_{\ell=1}^n\cos(2x_{j\ell}/m)^m
\right].
\tag{3}
```

For $`j\ne k`$ and $`s=\pm1`$, define

```math
G_{jk}^{(s)}=
e^{-(r_{jj}+r_{kk}+2s r_{jk})/m}
\cos(x_{jk}/m)^{2(m-1)}
\prod_{\ell\notin\{j,k\}}
\cos[(x_{j\ell}+s x_{k\ell})/m]^m.
\tag{4}
```

Then

```math
(V_m)_{P_jP_k}
=\frac m2\left(G_{jk}^{(-1)}-G_{jk}^{(+1)}\right).
\tag{5}
```

### Derivation

In the joint eigenbasis of the $`Q_j^{(m)}`$, a matrix element between eigenvalue vectors $`q,q'`$ is multiplied by

```math
\exp\left[
-\frac t2(q-q')^T R(q-q')
+it\,q^T B_0q'
\right].
\tag{6}
```

Flipping a single physical spin changes its group coordinate by $`\sqrt{2/m}`$. Averaging the phase over the other independent initial $`Z`$ values supplies the cosine factors in (1). Inserting one $`Z`$ in another group replaces one cosine by a sine and gives (2). Terms with two distinct spins in the same group give (3): equal-sign raising/lowering products have total coordinate change twice as large, while opposite-sign flips have zero group-coordinate change. For spins in different groups, the two relative flip signs give (4). Each of the two groups containing a flipped spin has $`m-1`$ unflipped spins, explaining the exponent $`2(m-1)`$. Their signed difference gives (5).

No Gaussian approximation is used in these formulas.

## 4. The finite-spin separability threshold

The collective operators satisfy

```math
[Q_j^{(m)},P_k^{(m)}]
=i\delta_{jk}\overline X_j^{(m)}.
```

For each party, define

```math
\Omega_X(a)=
\begin{pmatrix}
0&\mathrm{diag}(a_j:j\in X)\\
-\mathrm{diag}(a_j:j\in X)&0
\end{pmatrix}.
```

Every separable state obeys

```math
\mathrm{Tr}(W V_m)\ge
b_m(W,a):=
\sum_{X=A,B}
\mathrm{Tr}\left|
i\sqrt{W_X}\Omega_X(a)\sqrt{W_X}
\right|.
\tag{7}
```

This bound permits arbitrary entanglement among qubits within either party.

The full proof, including state-dependent commutators and the positive covariance of local means, is given in [the covariance witness account](covariance-witnesses.md). It permits arbitrary entanglement inside either party. In particular, finite spins are not assigned canonical commutators and no oscillator decoder is assumed to act on them.

## 5. Explicit convergence and a sufficient finite size

All constants below are fixed by $`C,t,W`$. Let

```math
X_{\max}=\max_{j,k}|x_{jk}|,
\qquad
m\ge\max\{1,4X_{\max}\}.
\tag{9}
```

Every trigonometric argument in (1)--(5) then has absolute value at most $`1/2`$, so its cosine is positive. Put

```math
u_j=\sum_\ell x_{j\ell}^2,\qquad
v_j=\sum_\ell x_{j\ell}^4,\qquad
A_j=r_{jj}+\frac{u_j}{2}.
```

For $`|z|\le1/2`$,

```math
0\le-\log\cos z-\frac{z^2}{2}\le\frac{z^4}{8},
\qquad
|\tan z-z|\le\frac{|z|^3}{2}.
\tag{10}
```

One direct proof uses $`\tan z\le 8z/7`$ for $`0\le z\le1/2`$, obtained from $`\sin z\le z`$ and $`\cos z\ge7/8`$. Integrating $`\tan^2 z`$ and then integrating once more gives constants $`64/147<1/2`$ and $`16/147<1/8`$.

### Magnetization error

Define

```math
\eta_j(m)=
\min\left\{1,\frac{A_j}{m}+\frac{v_j}{8m^3}\right\}.
```

Then

```math
0\lt a_j\le1,\qquad 0\le1-a_j\le\eta_j(m).
\tag{11}
```

Indeed $`-\log a_j=A_j/m+\epsilon_j`$ with $`0\le\epsilon_j\le v_j/(8m^3)`$, and $`1-e^{-z}\le z`$.

### Position and momentum error

For every pair $`j,k`$,

```math
\left|(V_m)_{Q_jP_k}-(V_\infty)_{Q_jP_k}\right|
\le
E^{QP}_{jk}(m):=
|x_{kj}|\eta_k(m)+\frac{|x_{kj}|^3}{2m^2}.
\tag{12}
```

This follows by writing
$`m a_k\tan(x_{kj}/m)-x_{kj} =x_{kj}(a_k-1)+m a_k[\tan(x_{kj}/m)-x_{kj}/m]`$.

### Diagonal momentum error

Write $`d_j=4A_j`$ and

```math
z_j^+(m)=\frac{d_j}{m}+\frac{2v_j}{m^3}.
```

Then

```math
\left|(V_m)_{P_jP_j}-(V_\infty)_{P_jP_j}\right|
\le
E^{PP}_{jj}(m):=
\frac{d_j}{2m}+\frac{v_j}{m^2}
+\frac m4[z_j^+(m)]^2.
\tag{13}
```

To see this, the negative logarithm of the product in (3) is $`z=d_j/m+\epsilon`$, with $`0\le\epsilon\le2v_j/m^3`$. The inequality
$`0\le e^{-z}-1+z\le z^2/2`$ holds for every $`z\ge0`$. Comparing $`(m-1)(1-e^{-z})/2`$ with $`d_j/2`$ gives (13).

### Off-diagonal momentum error

For $`j\ne k`$, set

```math
h_{jk}^{(s)}=
r_{jj}+r_{kk}+2s r_{jk}
+x_{jk}^2
+\frac12\sum_{\ell\notin\{j,k\}}
(x_{j\ell}+s x_{k\ell})^2,
```

```math
w_{jk}^{(s)}=
2x_{jk}^4+
\sum_{\ell\notin\{j,k\}}
(x_{j\ell}+s x_{k\ell})^4,
```

and

```math
z_{jk,s}^+(m)=
\frac{h_{jk}^{(s)}}m+
\frac{w_{jk}^{(s)}}{8m^3}.
```

Then

```math
\left|(V_m)_{P_jP_k}-(V_\infty)_{P_jP_k}\right|
\le
E^{PP}_{jk}(m):=
\frac{w_{jk}^{(+1)}+w_{jk}^{(-1)}}{16m^2}
+\frac m4
\left([z_{jk,+1}^+(m)]^2+[z_{jk,-1}^+(m)]^2\right).
\tag{14}
```

For the proof,

```math
-\log G_{jk}^{(s)}
=\frac{h_{jk}^{(s)}}m-\frac{x_{jk}^2}{m^2}
+\epsilon_{jk}^{(s)},
\qquad
0\le\epsilon_{jk}^{(s)}
\le\frac{w_{jk}^{(s)}}{8m^3}.
```

The common term $`-x_{jk}^2/m^2`$ cancels when the two signs are subtracted. Moreover,

```math
\frac{h_{jk}^{(+1)}-h_{jk}^{(-1)}}2
=2r_{jk}+\sum_\ell x_{j\ell}x_{k\ell}
=(V_\infty)_{P_jP_k}.
```

The exponent is nonnegative: the original factor in (4) lies in $`(0,1]`$, since $`R\succeq0`$. Apply the same exponential remainder bound to obtain (14).

### Witness error and threshold loss

The position covariance has no error. Define

```math
\begin{aligned}
\mathcal E_W(m)={}&
2\sum_{j,k}|W_{Q_jP_k}|E^{QP}_{jk}(m)\\
&+\sum_j W_{P_jP_j}E^{PP}_{jj}(m)
+2\sum_{j\lt k}|W_{P_jP_k}|E^{PP}_{jk}(m).
\end{aligned}
\tag{15}
```

Then

```math
\left|\mathrm{Tr}[W(V_m-V_\infty)]\right|
\le\mathcal E_W(m).
```

For each party let $`\eta_X(m)=\max_{j\in X}\eta_j(m)`$, and put

```math
\mathcal P_W(m)=
\mathrm{Tr}(W_A)\eta_A(m)
+\mathrm{Tr}(W_B)\eta_B(m).
\tag{16}
```

The reverse triangle inequality for the trace norm gives

```math
b_m(W,a)\ge b_\infty(W)-\mathcal P_W(m).
\tag{17}
```

Here
$`\|\Omega_X(a)-\Omega_X\|_{\mathrm{op}}=\max_{j\in X}|1-a_j|`$, and
$`\|\sqrt W K\sqrt W\|_1\le\mathrm{Tr}(W)\|K\|_{\mathrm{op}}`$.

A sufficient finite-size condition is therefore

```math
\boxed{\quad
m\ge\max\{1,4X_{\max}\},
\qquad
\mathcal E_W(m)+\mathcal P_W(m)<\Delta.
\quad}
\tag{18}
```

Every displayed error bound is $`O(1/m)`$. More explicitly it is a sum of nonnegative constant multiples of $`m^{-1},m^{-2},m^{-3},\ldots`$, apart from the harmless decreasing minimum in (11). Thus the sufficient bound decreases to zero. Starting above (9) and doubling $`m`$ terminates after finitely many steps, and every larger integer also satisfies (18) once it first holds. If the inputs and a positive lower bound on $`\Delta`$ are rational, this procedure can use rational arithmetic throughout.

The verifier [finite_spin_bounds.py](../verification/finite_spin_bounds.py) implements (9)--(18). For the original rational four-group example, the deliberately conservative theorem certifies $`m=16384`$. This is a proof of the general procedure, not a size claim: the sharper exact-moment certificate establishes the same example at $`m=512`$, hence 2048 physical qubits.

## 6. Exact finite constructions

### Four groups, 2048 qubits

Use the rational matrices and $`t=28/5`$ in [the rational four-group data](../verification/gaussian_exact_certificate.json). Each party contains two groups, and $`m=512`$. The exact-moment interval certificate gives

```math
\mathrm{Tr}(W V_m)\approx0.46469550158,
\qquad
b_m(W,a)\approx0.47663412934,
```

with a certified positive gap greater than $`0.01193862775480`$. The interval verifier uses rational endpoints, outward rounding, and adjacent alternating Taylor bounds. The positivity of $`C,C^\Gamma,W`$ is checked using exact principal minors.

### Eight-group lift of the integer covariance example

For the Werner–Wolf covariance $`G`$ specified in [the reservoir embedding](reservoir-embedding.md#an-explicit-integer-example), take

```math
R=G+\frac1{30}I,\qquad B_0=-\Omega,\qquad t=30.
```

Let $`W_T=N^TN`$ be its integer target witness with

```math
\mathrm{Tr}(W_TG)=26,\quad
\mathrm{Tr}W_T=30,\quad
b_T=28.
```

The corresponding carrier witness is

```math
W_C=\frac1{2t}M^T W_T M,\qquad
M=(-tB_0,\ I).
```

For the spin operators define the local extracted observable vector
$`X=(P-tB_0Q)/\sqrt{2t}`$. These are not exactly canonical spin operators. Instead their averaged commutator form is

```math
\Omega_X(a)=\frac12
\left[\mathrm{diag}(a)\Omega+\Omega\mathrm{diag}(a)\right].
```

In each target pair, its symplectic weight is

```math
c_k=\frac{a_{2k-1}+a_{2k}}2.
```

Since the two parties' local target witness blocks are diagonal, the valid finite-spin threshold simplifies to

```math
12(|c_1|+|c_2|)+2(|c_3|+|c_4|).
```

In the certified regime below, every magnetization is positive, so the absolute values reduce to the expression used by the verifier.

At $`m=16384`$, hence 131072 physical qubits, exact interval arithmetic proves

```math
\mathrm{Tr}(W_C V_m)\approx26.55959073682
<
27.15441771674,
```

with gap greater than $`0.59482697992167`$. This supplies a transparent finite-dimensional lift of the universal mechanism. The four-group example has the smaller certified qubit count. Neither count is asserted to be minimal.


The exact finite-spin calculations and their interval enclosures are reproducible using [the verification guide](../verification/README.md). The same moment formulas also support [uniform parameter-robustness certificates](robustness.md).
