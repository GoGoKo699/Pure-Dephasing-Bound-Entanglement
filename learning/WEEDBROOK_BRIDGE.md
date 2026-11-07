# From Gaussian quantum information to pure-dephasing bound entanglement

[Thirty-milestone map](MILESTONES.md) · [Scientific overview](../science/README.md) · [Exact verification](../verification/README.md)

Dephasing leaves the populations in a preferred basis unchanged. With classical correlated phase noise, each realization is a product of local phase rotations, so a separable system stays separable. This project asks what changes when the dephasing reservoir supplies quantum correlations: can an initially product system become entangled while remaining positive under partial transpose across the same bipartition at every time?

The construction answers that question affirmatively. Its explanation has three layers. Gaussian covariance matrices identify a suitable reservoir resource. A special dephasing channel transfers its correlations into oscillator carriers without changing their position populations. An independent finite-spin argument then establishes the effect for actual qubits. A PPT test and a separability witness play different roles throughout: one protects positivity under partial transpose, while the other proves entanglement.

The single educational anchor is **Christian Weedbrook et al., Gaussian Quantum Information**, [arXiv:1110.3234v1][weedbrook], associated with *Reviews of Modern Physics* **84**, 621–669 (2012), [DOI:10.1103/RevModPhys.84.621](https://doi.org/10.1103/RevModPhys.84.621). This bridge uses the section numbering of that checked author version. The primary sources for the imported theorems, dephasing model and comparisons are separately credited in [Related work](../references/RELATED_WORK.md).

## A focused route through the anchor

The relevant sections connect directly to the objects used below; the rest of the review is not needed for this route.

| Weedbrook section | Foundation used here | Connection to this project |
|---|---|---|
| I D; II A | Quadrature normalization and oscillator modes | Fix the commutator convention and count physical modes correctly. |
| II A.1 | First moments, covariance and quantum uncertainty | Describe the target, carrier vacuum and exact Gaussian output. |
| II A.2; II B.3–4; II B.6 | Gaussian unitaries, squeezing, rotations and beam splitters | Interpret the local canonical decoder and its physical resources. |
| II C, especially II C.2 | Symplectic structure and decomposition of canonical transformations | Distinguish a genuine subsystem extraction from a formal matrix manipulation. |
| II D.1 | Separability and partial transpose | Understand why PPT alone leaves the relevant entanglement question undecided. |
| II D.2 | Negativity and distillation | Interpret zero negativity and the nondistillability of PPT entanglement. |
| II E.1 | Homodyne measurement | Relate the oscillator witness to measurements of quadrature fluctuations. |
| V A | Gaussian channels, dilation and complete positivity | Identify the roles of drift, noise and reservoir degrees of freedom. |

The project-specific derivations begin in [the dephasing model](../science/model.md). The anchor supplies their Gaussian language, while the exact semigroup correspondence and finite-spin bounds are established in the repository.

## Conventions that carry the same covariance

Weedbrook's quadrature vector, denoted here by $x_W$, satisfies

$$
[x_{W,j},x_{W,k}]=2i\Omega_{jk},
\qquad
(V_W)_{jk}=\frac12\langle\{\Delta x_{W,j},\Delta x_{W,k}\}\rangle.
$$

Its vacuum has $V_W=I$. The project rescales the physical quadratures and changes the covariance definition together:

$$
z=\frac{x_W}{\sqrt2},
\qquad
[z_j,z_k]=i\Omega_{jk},
\qquad
V_{jk}=\langle\{\Delta z_j,\Delta z_k\}\rangle.
$$

Substituting the rescaling shows that **$V=V_W$ numerically**, provided the coordinate ordering is the same. Both descriptions therefore use

$$
V_{\mathrm{vac}}=I,
\qquad V+i\Omega\succeq0.
$$

The physical single-quadrature variance is different: in the project's convention a vacuum quadrature has variance $1/2$, and a covariance diagonal entry is twice that variance. For any real coefficient vector $f$,

$$
f^{\mathsf T}Vf=2\operatorname{Var}(f^{\mathsf T}z).
$$

That factor of two matters in the worked witness below. A quoted witness score is a sum of **doubled** variances. Gaussian channel formulas retain the same matrix form after the coordinated rescaling: if the anchor uses $V_W\mapsto TV_WT^{\mathsf T}+N$, the project's doubled covariance transforms by the same numerical $T,N$.

Coordinate ordering is a separate issue. The target uses canonical pairs ordered by party, such as $(q_1,p_1,q_2,p_2,\ldots)$. The carrier covariance is usually written with all positions followed by all momenta, $(Q_1,\ldots,Q_d,P_1,\ldots,P_d)$. Permuting the coordinates also permutes the covariance and commutator matrices. Numerical equality of conventions never licenses keeping one matrix fixed while silently changing its ordering. The precise definitions are in [model — Oscillator evolution](../science/model.md#oscillator-evolution) and [embedding — Conventions and theorem](../science/reservoir-embedding.md#conventions-and-theorem).

## Three roles and one fixed partition

A **target** is a centered Gaussian state whose correlations are described by a real covariance $G$. It has $r$ canonical modes and therefore $2r$ quadrature coordinates. In the local dilation, the reservoir is supplied in this target state. Its coordinates are called $Z$, with commutator matrix $\Omega=\Omega_A\oplus\Omega_B$.

The **carriers** are different physical oscillators, initially in product vacuum. The construction introduces $d=2r$ carriers, one carrier position $Q_j$ for each target phase-space coordinate $Z_j$. Thus the vector $Q$ consists of commuting operators even though the vector $Z$ does not. Each carrier also has its conjugate momentum $P_j$. Alice and Bob own the carriers corresponding to their respective target coordinates. A four-mode target with two modes per party therefore uses eight carrier oscillators, four per party.

The **finite-spin groups** are a further realization. Each carrier position is replaced by a normalized collective spin component of a group of qubits. Those groups are not exact bosonic modes: their conjugate collective observables have operator-valued commutators. Their validity is proved later through exact moments and an appropriate uncertainty bound.

Locality always refers to the same chosen Alice–Bob partition. An operation mixing two of Alice's modes remains local across that partition. Conversely, even when each basis observable $Q_j$ belongs to one party, a Lindblad jump obtained by factoring the coefficient matrix can combine several $Q_j$ from both parties. Group-local observables therefore do not imply spatially local jump operators. The [model](../science/model.md#question-and-conventions) keeps these distinctions explicit.

## What the dephasing channel does

For commuting Hermitian carrier positions, use

$$
\mathcal L_C(\rho)=\sum_{j,k}C_{jk}
\left(Q_j\rho Q_k-\frac12\{Q_kQ_j,\rho\}\right),
\qquad C=R+iB\succeq0,
$$

where $R$ is real symmetric and $B$ is real antisymmetric. The original system Hamiltonian is zero. In the common position basis, its exact action is

$$
\rho_t(x,y)=
\exp\left[-\frac t2(x-y)^{\mathsf T}R(x-y)
+itx^{\mathsf T}By\right]\rho_0(x,y).
$$

For $x=y$ the exponent is zero, so every joint position-basis population is preserved. For off-diagonal matrix elements, the real part damps coherence and the imaginary part supplies a phase depending on both position labels. Multiplying the kernels adds their times, giving the semigroup composition law. When $B=0$, the same channel can be written as a classical Gaussian average of local phase rotations and cannot entangle a separable input. These statements follow directly from [the exact kernel](../science/model.md#exact-dephasing-kernel).

Fixed positions do not imply fixed oscillator energy. From product vacuum, the doubled covariance is

$$
V_t=\begin{pmatrix}
I&-tB\\
tB&I+2tR-t^2B^2
\end{pmatrix}.
$$

Position variance stays fixed, while position–momentum correlations and momentum variance change. The associated drift is generally not symplectic by itself. The diffusion is essential to satisfy the complete-positivity condition reviewed in Weedbrook §V A and checked explicitly in [Oscillator evolution](../science/model.md#oscillator-evolution).

## Encoding and locally revealing the target

Set the overall dephasing rate to one, so time is measured in its inverse-rate units. Choose $R=G$ and $B=-\Omega$, so that

$$
C_G=G-i\Omega.
$$

The target uncertainty condition is $G+i\Omega\succeq0$. Because $G$ is real, complex conjugation gives $C_G\succeq0$. A valid target covariance has therefore supplied a valid dephasing coefficient matrix.

The mechanism becomes transparent in the finite-time dilation

$$
U_t=\exp\left(i\sqrt{2t}\,Q^{\mathsf T}Z\right),
\qquad
P_{\mathrm{out}}=P-t\Omega Q+\sqrt{2t}\,Z.
$$

The interaction splits into an Alice term and a commuting Bob term. It is local on the enlarged parties consisting of each party's carriers and reservoir. The resulting carrier channel is the dephaser above, after the reservoir is traced out. This is a dilation of each channel at a specified time; composing channels uses fresh reservoir degrees of freedom. The factor $\sqrt t$ does not describe repeatedly reusing one finite bath under one fixed interaction for physical duration $t$. The complete derivation is in [Exact channel and a finite-time dilation](../science/reservoir-embedding.md#exact-channel-and-a-finite-time-dilation).

Consider the carrier observables

$$
X=\frac{P+t\Omega Q}{\sqrt{2t}}.
$$

They have the canonical target commutators, and the dilation gives a simple output identity:

$$
[X_j,X_k]=i\Omega_{jk},
\qquad
X_{\mathrm{out}}=Z+\frac{P_{\mathrm{in}}}{\sqrt{2t}}.
$$

The initially independent carrier momenta add covariance $I/(2t)$, so the extracted Gaussian state has covariance

$$
G_{\mathrm{out}}=G+\frac{I}{2t}.
$$

Canonical commutators alone are not the whole subsystem argument. The proof supplies a complement $Y=(P-t\Omega Q)/\sqrt{2t}$ that commutes with $X$. Its commutator form is $-\Omega$; reversing the momentum labels in each complementary pair gives a canonical $Y'$. The full transformation from $(Q,P)$ to $(X,Y')$ is symplectic and local across the chosen parties. Local tracing of $Y'$ therefore exposes a genuine target-sized subsystem. Squeezing, a Fourier rotation and a balanced beam splitter within each party implement this transformation. The [canonical completion](../science/reservoir-embedding.md#local-canonical-extraction-and-completion) provides the matrix proof.

If the extracted state is entangled, the original carrier state was already entangled: local Gaussian unitaries and local discarding cannot create entanglement across the partition. The decoder can thus serve as a proof device, with its variance witness pulled back to the original carriers.

## A complete eight-carrier example

### Exact inputs and the PPT guarantee

Take a four-mode target in the order

$$
Z=(q_1,p_1,q_2,p_2,q_3,p_3,q_4,p_4)^{\mathsf T},
\qquad A=(1,2),\qquad B=(3,4).
$$

The inherited Werner–Wolf covariance $G_0$ is fully specified by

$$
\operatorname{diag}(G_0)=(2,1,2,1,2,4,2,4)
$$

and the following nonzero upper off-diagonal entries, with one-based indices:

$$
(G_0)_{15}=1,\qquad
(G_0)_{28}=(G_0)_{37}=(G_0)_{46}=-1.
$$

Its lower off-diagonal entries follow by symmetry; every other off-diagonal entry is zero. Let $\Omega$ consist of four canonical two-by-two blocks, and let $\Omega_{\mathrm{PT}}$ reverse the first two blocks. Both $G_0+i\Omega$ and $G_0+i\Omega_{\mathrm{PT}}$ have eigenvalues

$$
0,\quad 3,\quad 3-\sqrt3,\quad 3+\sqrt3,
$$

each twice. They are positive semidefinite. The source covariance, its matrix and the exact spectral certificate are given in [An explicit integer example](../science/reservoir-embedding.md#an-explicit-integer-example), with attribution to Werner and Wolf's Eq. (9).

Set

$$
G=G_0+\frac1{30}I,
\qquad C=G-i\Omega,
\qquad t=30.
$$

Adding $I/30$ makes the physicality and PPT uncertainty matrices strictly positive. Use eight carrier vacua, four held by each party, and the zero-Hamiltonian dephasing generator with this $C$. The transformed coefficient matrix is congruent to $G-i\Omega_{\mathrm{PT}}$, so the channel preserves PPT at every time. This claim is independent of the witness calculation that follows.

### Four variances and their separable threshold

On the extracted four-mode system, define

$$
\begin{aligned}
L_1&=2q_1-q_3,& L_2&=2q_2+q_4,\\
L_3&=3p_1+p_4,& L_4&=3p_2+p_3.
\end{aligned}
$$

The score is the sum of doubled variances,

$$
\mathcal S=2\sum_{j=1}^{4}\operatorname{Var}(L_j)
=\operatorname{Tr}(WG),
$$

when evaluated on a covariance $G$, with $W$ the sum of the four coefficient-vector outer products. This representation makes $W\succeq0$ immediate.

For a product state across Alice and Bob, cross-party covariances vanish. The local Alice terms have weights 4 on each position and 9 on its momentum. With doubled variances $v_q,v_p$, local uncertainty gives $v_qv_p\geq1$, hence

$$
4v_q+9v_p\geq2\sqrt{36v_qv_p}\geq12.
$$

Alice has two modes, contributing at least 24. Bob has weight 1 on both quadratures of each of two modes, contributing at least 4. A separable mixture adds a positive covariance of the component means and cannot lower the score. Thus every separable state with finite second moments satisfies

$$
\mathcal S\geq28.
$$

This argument allows arbitrary states and arbitrary entanglement inside either party; it does not restrict the separable alternatives to Gaussian states. The general form is proved in [The witness bound](../science/covariance-witnesses.md#the-witness-bound).

For $G_0$, the four doubled variances are $6,6,7,7$, totaling 26. For example, the first is $4(G_0)_{11}+(G_0)_{55}-4(G_0)_{15}=8+2-4=6$. The squared coefficient norms of the four observables are $5,5,10,10$, so isotropic added covariance $\eta I$ raises the score by $30\eta$.

### Finite-time output, measurement and conclusion

At the chosen time, target noise and extraction noise add:

$$
G_{\mathrm{out}}
=G_0+\left(\frac1{30}+\frac1{60}\right)I
=G_0+\frac1{20}I.
$$

The score is therefore

$$
\mathcal S=26+30\left(\frac1{20}\right)
=\frac{55}{2}=27.5<28.
$$

The strict witness gap is $1/2$. Together with the separately established all-time PPT property, this certifies a PPT-entangled carrier state at $t=30$. The entanglement already exists before any decoder or measurement is performed.

The measurements have a direct interpretation. After local decoding, quadrature measurements on repeated preparations estimate the four variances. Alice and Bob can combine their local measurement records to form each cross-party linear combination. Position and momentum settings use separate preparations when they are incompatible. Alternatively, substitute $X=(P+30\Omega Q)/\sqrt{60}$ into each $L_j$ and measure the corresponding carrier observables; no physical decoder is required for that pulled-back witness. Measurement results certify the unconditional output and are not postselected to prepare it. Weedbrook §II E.1 supplies the oscillator measurement background.

The resources remain visible. The local dilation supplies a four-mode reservoir in state $G$, which is itself PPT entangled. Physical decoding includes local squeezing and mode mixing. At this benchmark the total carrier excitation above the eight uncoupled vacua is 2074, as follows from [the stated energy formula](../science/reservoir-embedding.md#resources-interpretation-and-limitations). This finite-energy mathematical construction does not assert a laboratory optimum.

## From the example to the full result

The example provides one strict witness. The universal theorem needs two further arguments, each with a different quantifier.

For a **separable Gaussian target**, the Werner–Wolf covariance criterion supplies physical local covariances with $G\succeq G_A\oplus G_B$. Writing $N=G-(G_A\oplus G_B)\succeq0$ gives

$$
C_G=(G_A-i\Omega_A)\oplus(G_B-i\Omega_B)+N.
$$

The first part generates local channels; the real positive remainder generates shared classical phase kicks. Alternatively, a separable reservoir in the local dilation cannot create cross-party entanglement. This proves preservation for **every separable carrier input**, including non-Gaussian inputs.

For an **entangled Gaussian target**, separation of the closed, upward-closed Gaussian separability covariance set supplies a positive witness $W$ with strict gap

$$
\Delta=\beta_{\mathrm{sep}}(W)-\operatorname{Tr}(WG)>0.
$$

The extracted output adds only $\operatorname{Tr}W/(2t)$ to its score, so entanglement is certain whenever

$$
t>\frac{\operatorname{Tr}W}{2\Delta}.
$$

This converse only needs one suitable product input, supplied by carrier vacuum at sufficiently large finite time. The existence of a strict positive covariance witness is a mathematical ingredient, not a consequence of small noise alone. The closedness, separation argument and all-state witness validity are supplied in [Separability: both directions](../science/reservoir-embedding.md#separability-both-directions) and [Covariance witnesses](../science/covariance-witnesses.md).

For PPT, the transformed coefficient matrix satisfies

$$
SC_TS=G-i\Omega_{\mathrm{PT}},
\qquad S=(-I_A)\oplus I_B.
$$

Thus a PPT target gives a PPT-preserving semigroup. If the target is NPT, its partially transposed uncertainty matrix has a negative eigenvalue that survives sufficiently small positive scalar noise. Local extraction then produces an NPT state from a product input at a finite time, proving the converse. These equivalences apply to the encoded family; the general transformed-generator test is only asserted as sufficient outside it. See [PPT: exact covariance-to-generator correspondence](../science/reservoir-embedding.md#ppt-exact-covariance-to-generator-correspondence).

At any prescribed $t>0$, independently squeezed carrier inputs with doubled momentum covariance $sI$ change the extracted covariance to $G+sI/(2t)$. A sufficiently small but positive $s$ therefore yields the fixed-time converses. It also supplies an explicit input-energy cost. Vacuum at large time and squeezed inputs at fixed time are distinct statements; neither provides exact noiseless recovery at finite time.

## Why the finite-qubit result needs another proof

The oscillator construction offers a design, but finite spins have different algebra. For each group of $m$ qubits, set

$$
Q_j^{(m)}=\frac{\sum_{a=1}^{m}Z_{ja}}{\sqrt{2m}},
\qquad
P_j^{(m)}=-\frac{\sum_{a=1}^{m}Y_{ja}}{\sqrt{2m}},
\qquad
\overline X_j^{(m)}=\frac1m\sum_{a=1}^{m}X_{ja}.
$$

The initial state is the product of $|+\rangle$ over all physical qubits. Its collective doubled covariance is the oscillator vacuum covariance, but the exact commutator is

$$
[Q_j^{(m)},P_k^{(m)}]=i\delta_{jk}\overline X_j^{(m)}.
$$

During evolution the magnetizations $a_j=\langle\overline X_j^{(m)}\rangle$ change. The same coefficient matrices still give complete positivity and all-time PPT for these bounded commuting dephasing observables. What requires new work is the entanglement witness.

The [exact moment derivation](../science/finite-spin-transfer.md#3-exact-finite-spin-moments) evaluates the dephasing kernel on one- and two-spin flips. A single flip changes its group coordinate by $\sqrt{2/m}$. Averaging the resulting phases over the other initially independent spins produces cosine factors. This yields finite-$m$ formulas without assuming a Gaussian state. Their covariance enters a separability bound using the **actual** commutator matrix $\Omega_X(a)$ on each party:

$$
\operatorname{Tr}(WV_m)\geq
\sum_{X=A,B}\operatorname{Tr}
\left|i\sqrt{W_X}\,\Omega_X(a)\sqrt{W_X}\right|
=b_m(W,a).
$$

The bound follows by averaging the local uncertainty inequalities of a separable mixture. Commutator expectations are linear in the state, while covariance of the component means is positive. It therefore remains valid for every finite-spin separable state, even with internal entanglement within either party. Replacing $a_j$ by one would lose this guarantee. The proof is in [The finite-spin separability threshold](../science/finite-spin-transfer.md#4-the-finite-spin-separability-threshold).

To transfer a strict oscillator witness, both its score and threshold must be controlled. The finite-spin theorem supplies a score-error bound $\mathcal E_W(m)$ and a threshold-loss bound $\mathcal P_W(m)$, each tending to zero as $O(1/m)$. Once their stated argument-domain condition holds, the sufficient criterion is

$$
\mathcal E_W(m)+\mathcal P_W(m)<\Delta.
$$

Their monotone bounds give a computable finite group size after which every larger integer also works. This is convergence of the relevant moments and witness, rather than a claim of trace-norm convergence across different Hilbert spaces. The [explicit error bounds](../science/finite-spin-transfer.md#5-explicit-convergence-and-a-sufficient-finite-size) provide the missing finite-size step.

The smaller explicit realization uses the separate rational **four-carrier** construction, with four groups of 512 qubits and time $28/5$. Its exact-moment interval certificate gives a strict gap greater than **0.01193862775480** across 1024 versus 1024 qubits. Its displayed score is approximately 0.46469550158 and its state-dependent separability threshold approximately 0.47663412934; outward rational intervals, rather than those rounded decimals, establish the inequality. The general sufficient-size bound is more conservative, at 16,384 qubits per group for the same coefficient data. The eight-carrier integer example also has a separate finite-spin realization. These results and their distinct roles are recorded in [Exact finite constructions](../science/finite-spin-transfer.md#6-exact-finite-constructions).

## What is retained in the complete claim

The Gaussian construction and the spin construction use the same logical structure: positivity of two coefficient matrices gives physical, all-time PPT dynamics; a separate all-state covariance witness proves entanglement at a finite time. The conserved quantity is the joint dephasing-basis population. Quantum-correlated reservoirs, collective couplings, conjugate-observable fluctuations and energy are not removed by that conservation law.

The [robustness result](../science/robustness.md) gives two separate nonzero parameter neighborhoods for the 2048-qubit certificate: an independent-entry coefficient box of radius $10^{-4}$ with the matrix symmetries retained, and added local group dephasing rates up to $1/200$. Their maximum perturbations are not combined into an unproved simultaneous guarantee. They concern the specified generator model, not independent noise on each physical qubit or arbitrary experimental imperfections.

All entanglement and PPT statements refer to the same designated bipartition. A different cut may become NPT. Physical target extraction includes the local decoder and its resources, whereas witness certification can use its pullback. The target reservoir carries entanglement; the result does not create it from a globally uncorrelated system-plus-environment state.

The anchor explains Gaussian states, symplectic transformations, PPT and channels. The additional steps supplied here are the commuting-position semigroup, its local extraction and exact correspondences, an all-state witness adapted to actual spin commutators, and controlled finite-size and robustness estimates. Established Gaussian bound entanglement, dissipative reservoir transfer, PPT-preserving Gaussian entangling channels and boson–spin correspondences retain their primary attributions in [Related work](../references/RELATED_WORK.md). The [scientific overview](../science/README.md#how-the-proofs-fit-together) connects the authoritative proofs, and the [verification guide](../verification/README.md) connects their exact instances to executable certificates.

[weedbrook]: https://arxiv.org/abs/1110.3234v1
