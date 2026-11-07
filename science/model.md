# Pure dephasing and its partial transpose

[Scientific route](README.md) · [Covariance witnesses](covariance-witnesses.md)

## Question and conventions

Can a Markovian evolution create entanglement while every state on its trajectory remains positive under partial transpose? The answer depends on the allowed dynamics. This project establishes the effect inside the restricted class of **pure dephasing with no Hamiltonian**, starting from an individually factorized system state. The relevant bipartition is fixed throughout each claim.

Let the mutually commuting Hermitian observables $Q_1,\ldots,Q_d$ each belong entirely to party A or party B. We use the generator

$$
\mathcal L_C(\rho)=\sum_{j,k=1}^{d}C_{jk}\left(Q_j\rho Q_k-\frac12\{Q_kQ_j,\rho\}\right),\qquad C=R+iB\succeq0,
$$

where $R=R^{\mathsf T}$ and $B=-B^{\mathsf T}$ are real. There is no original Hamiltonian term. Positivity of the coefficient matrix makes this a Lindblad generator for bounded observables. For oscillator positions, the Gaussian channel below supplies a well-defined channel formulation, and the [reservoir embedding](reservoir-embedding.md) has an explicit dilation.

The $Q_j$ are local basis observables. The actual Lindblad jumps obtained by factoring $C$ can be complex collective combinations of several $Q_j$, spanning both parties. Locality of each basis observable is therefore not a claim of spatially local jumps or independent classical noise. These conventions follow the correlated-dephasing framework of [Seif, Wang and Clerk (2022)](../references/RELATED_WORK.md#correlated-dephasing-and-the-open-question).

## Exact dephasing kernel

In the joint eigenbasis, write $x,y$ for two real eigenvalue vectors. Then

$$
\rho_t(x,y)=\exp\left[-\frac t2(x-y)^{\mathsf T}R(x-y)+itx^{\mathsf T}By\right]\rho_0(x,y).
$$

To obtain the exponent, insert the eigenvalues into the generator. The imaginary parts of $x^{\mathsf T}Cx$ and $y^{\mathsf T}Cy$ vanish by antisymmetry. Every diagonal matrix element is fixed, and the exponents add under composition, so the channels form a time-homogeneous semigroup. The same expression is a kernel identity for oscillator positions.

If $B=0$, the channel is an average over real Gaussian phase kicks. Every kick factorizes across the two parties, even when the classical phases are correlated. Such a channel preserves separability. The construction retains the quantum noise correlations encoded by complex $C$.

## A sufficient all-time PPT condition

Partial transpose is taken on A in the eigenbasis of its $Q_j$. Order the group indices by party. Define

$$
C_T=\begin{pmatrix}
R_{AA}-iB_{AA}&-R_{AB}\\
-R_{BA}&R_{BB}+iB_{BB}
\end{pmatrix}.
$$

**Proposition 1.** If both $C\succeq0$ and $C_T\succeq0$, the channel $\Phi_t=\exp(t\mathcal L_C)$ preserves PPT across A versus B for every $t\geq0$.

**Proof.** Transposing the A factors in the generator yields

$$
T_A\mathcal L_C T_A=\mathcal L_{C_T}-i[H_T,\,\cdot\,],\qquad
H_T=\sum_{j\in A,\,k\in B}B_{jk}Q_jQ_k.
$$

The local A coefficient block is transposed. The real cross-party block changes sign, while the imaginary cross-party terms give the displayed Hermitian Hamiltonian. If $C_T\succeq0$, this conjugated generator defines a completely positive, trace-preserving evolution. Because $T_A^2$ is the identity,

$$
T_A\Phi_tT_A=\exp(tT_A\mathcal L_CT_A)
$$

is completely positive. Applying it to $T_A\rho\succeq0$ proves $T_A\Phi_t(\rho)\succeq0$. The oscillator realization follows from its Gaussian-channel matrices, or from the local dilation for the embedding family. $H_T$ is a mathematical feature of the transpose-conjugated evolution; it is not an interaction added to the original dynamics. This criterion is inherited from the cited correlated-dephasing work. $\square$

This proposition gives the PPT guarantee. A separate separability witness is needed to establish entanglement; positivity under partial transpose alone cannot decide that question.

## Oscillator evolution

For $d$ carrier oscillators, take $Q_j=q_j$, $P_j=p_j$, with $[q_j,p_k]=i\delta_{jk}$. Use the doubled covariance convention

$$
V_{ab}=\langle\{r_a-\langle r_a\rangle,r_b-\langle r_b\rangle\}\rangle,\qquad r=(q_1,\ldots,q_d,p_1,\ldots,p_d)^{\mathsf T}.
$$

The product vacuum has $V_0=I_{2d}$, and physical covariances satisfy $V+i\Omega_d\succeq0$, where

$$
\Omega_d=\begin{pmatrix}0&I_d\\-I_d&0\end{pmatrix}.
$$

The Heisenberg equations and diffusion give

$$
\dot q=0,\qquad \dot p=Bq,\qquad
V(t)=\begin{pmatrix}I_d&-tB\\tB&I_d+2tR-t^2B^2\end{pmatrix}.
$$

More generally, the Gaussian channel acts as $V\mapsto X_tVX_t^{\mathsf T}+Y_t$, with

$$
X_t=\begin{pmatrix}I_d&0\\tB&I_d\end{pmatrix},\qquad
Y_t=\begin{pmatrix}0&0\\0&2tR\end{pmatrix}.
$$

These matrices obey the channel composition law and

$$
Y_t+i\Omega_d-iX_t\Omega_dX_t^{\mathsf T}
=\begin{pmatrix}0&0\\0&2tC^{\mathsf T}\end{pmatrix}\succeq0.
$$

This verifies complete positivity directly, without interpreting an unbounded formal generator as a proof of existence. The drift $p\mapsto p+tBq$ is generally not symplectic by itself: the associated diffusion is essential.

## What is conserved and what is supplied

All joint dephasing-basis populations are constant. For spins, these are computational-basis populations. For oscillators, these are position-basis populations; oscillator energy can grow because momentum variance grows. The system begins without entanglement. The environment supplies quantum correlations, and their explicit role is shown by the reservoir dilation. The result concerns unconditional reduced dynamics: no bath monitoring or outcome postselection is required.

PPT entanglement cannot be distilled into Bell pairs by local operations and classical communication across the specified cut. A claim of PPT across this cut says nothing about a different partition of the same groups. The finite construction and its quantified qualifications are given in [the four-mode certificate](four-mode-certificate.md) and [the finite-spin transfer](finite-spin-transfer.md).
