# A four-mode certificate and 2,048-qubit realization

[Scientific route](README.md) · [Covariance witness](covariance-witnesses.md) · [Finite-spin theorem](finite-spin-transfer.md)

The [reservoir embedding](reservoir-embedding.md) gives a general mechanism and a simple integer example. The construction here uses only four oscillator carriers and supplies the smaller explicit finite-qubit realization. It does not assert a minimum number of qubits.

## The coefficient matrix

Alice holds groups 1 and 2; Bob holds groups 3 and 4. In the [dephasing model](model.md), set

```math
R=\frac1{1000}\begin{pmatrix}
1491&-316&-92&484\\
-316&168&-13&-355\\
-92&-13&480&542\\
484&-355&542&1874
\end{pmatrix},
```

```math
B=\frac1{1000}\begin{pmatrix}
0&237&-525&-1597\\
-237&0&246&265\\
525&-246&0&267\\
1597&-265&-267&0
\end{pmatrix},\qquad C=R+iB.
```

All rates are given in the same arbitrary inverse-time unit. The observation time is $`t_*=28/5`$. The original Hamiltonian is zero. These matrices are input data, rather than rounded display versions of an unrecorded model.

## Exact physicality and all-time PPT

Sylvester's criterion applies because $`C`$ and $`C_T`$ are Hermitian. Their leading principal minors, in increasing order, are

```math
\mathrm{minors}(C)=\left(\frac{1491}{1000},\frac{94463}{10^6},\frac{1963499}{10^9},\frac{1415751}{125000000000}\right),
```

```math
\mathrm{minors}(C_T)=\left(\frac{1491}{1000},\frac{94463}{10^6},\frac{42912437}{10^9},\frac{760454679}{200000000000}\right).
```

Every entry is strictly positive. Thus the physical generator and its transpose-conjugated generator are completely positive, for either oscillator or finite-spin group observables. Starting from a product state, the output remains PPT across groups 1,2 versus groups 3,4 at every nonnegative time.

## Entanglement of the oscillator output

Prepare four product vacuum modes. Let $`W`$ be the exact rational eight-by-eight matrix `W_integer_100000 / 100000` in [the certificate data](../verification/gaussian_exact_certificate.json), using the order $`(q_1,q_2,q_3,q_4,p_1,p_2,p_3,p_4)`$. Its eight leading principal minors are exactly positive; the verifier reconstructs them from the matrix.

For the evolved covariance $`V(t_*)`$, the exact score is

```math
\mathrm{Tr}[WV(t_*)]=\frac{35995891709}{78125000000}=0.4607474138752.
```

The local principal blocks use indices $`(1,2,5,6)`$ for A and $`(3,4,7,8)`$ for B, with one-based indexing. Applying the two-mode radical formula in [the covariance witness proof](covariance-witnesses.md) gives the following strict rational lower bounds:

```math
f_A>\frac{16089}{50000},\qquad f_B>\frac{4309}{25000},\qquad f_A+f_B>\frac{24707}{50000}=0.494140.
```

For reproducibility, the local radical invariants are

```math
s_A=\frac{11795607}{625000000},\quad d_A=\frac{1229466375031889}{10^{20}},
```

```math
s_B=\frac{43460103}{10^{10}},\quad d_B=\frac{237316142885267}{10^{20}}.
```

The inequalities follow by squaring nonnegative rational quantities in $`2\sqrt{s+2\sqrt d}`$. Their combination proves a strict separability-witness gap

```math
f_A+f_B-\mathrm{Tr}[WV(t_*)]>\frac{2608795791}{78125000000}=0.0333925861248.
```

The witness excludes every separable state with finite second moments. Together with the all-time PPT property, this proves bound entanglement at the stated time.

## An exact finite-qubit realization

Replace each group by $`m=512`$ qubits and use

```math
Q_j=\frac{\sum_{a=1}^{512}Z_{ja}}{\sqrt{1024}},\qquad
P_j=-\frac{\sum_{a=1}^{512}Y_{ja}}{\sqrt{1024}}.
```

The same $`C`$ defines the evolution. Its initial state is $`|+\rangle^{\otimes2048}`$, so even the individual qubits begin unentangled. A holds the first 1,024 qubits and B the last 1,024. Exact finite-spin moments and the actual magnetizations in the local uncertainty bounds yield:

| Group size | Total qubits | Witness score, approximate | Separable threshold, approximate | Certified strict gap |
|---|---:|---:|---:|---:|
| 512 | 2,048 | 0.46469550158 | 0.47663412934 | greater than 0.01193862775480 |
| 1,024 | 4,096 | See exact output | See exact output | greater than 0.02769832851354 |

The decisive comparisons use outward-rounded rational intervals, not the displayed decimals or a floating-point eigensolver. See [the exact output](../verification/independent_dephasing_certificate.json) and [finite-size proof](finite-spin-transfer.md). In particular, the calculation does not assume canonical spin commutators and does not construct a matrix of dimension $`2^{2048}`$.

The certificate uses the specified bipartition. It does not certify PPT across all partitions of the four groups. It establishes an explicit size, not an optimum. Quantified coefficient and added-dephasing perturbations are covered by [the robustness certificate](robustness.md).

## Reproduction

From the repository root:

```bash
python verification/independent_dephasing_certificate.py
```

The program reconstructs $`C,C_T,W`$, checks exact positive minors, verifies the oscillator radicals, and encloses the finite-spin scores and thresholds. Its only nonstandard dependency is SymPy. Run without Python's `-O` option; the script rejects optimized execution rather than disabling its assertions. The [verification guide](../verification/README.md) explains dependencies, outputs, and the distinction between symbolic proofs and tested numerical instances.
