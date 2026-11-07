# Thirty milestones for pure-dephasing bound entanglement

[Scientific overview](../science/README.md) · [Weedbrook bridge](WEEDBROOK_BRIDGE.md) · [Exact verification](../verification/README.md)

This map follows the scientific structure of the project: local quantum observables lead to bipartite covariance criteria; a constrained dephasing mechanism then turns those criteria into a dynamical correspondence and finite-qubit certificates. The single educational anchor is **Weedbrook et al., Gaussian Quantum Information**, using [arXiv:1110.3234v1][weedbrook], associated with *Reviews of Modern Physics* **84**, 621–669 (2012). Below, **W** denotes that source and its section numbering. The [bridge](WEEDBROOK_BRIDGE.md) translates conventions and supplies the project-specific steps. Primary research attributions remain in [Related work](../references/RELATED_WORK.md).

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. Twelve background targets connect single-mode kinematics, local operations, separability, partial transpose, witnesses and channels into the question the construction must answer. Eighteen further targets are needed because the result joins a Gaussian embedding, two converse arguments, exact examples and a separate finite-spin theorem. Each phase ends by connecting its components into a complete claim. The map covers the load-bearing understanding targets; detailed estimates and algebra remain in their authoritative scientific pages.

## Phase I — Background and preliminaries: M01–M12

### M01 — A mode and its quadratures

- **Central question:** What makes a pair of observables one oscillator mode?
- **Understanding target:** The canonical commutator fixes the quantum uncertainty scale. Weedbrook's quadratures have commutator $2i$; the project uses $i$ and a doubled covariance.
- **Dependencies and story role:** Starting point. It fixes the local object before matrices or multipartite states are introduced.
- **Conceptual connection:** The same numerical vacuum covariance can accompany different operator normalizations. This distinction controls every later witness threshold.
- **Source pointers:** [W, §§I D and II A][weedbrook]; [model — Oscillator evolution](../science/model.md#oscillator-evolution); [bridge — Conventions that carry the same covariance](WEEDBROOK_BRIDGE.md#conventions-that-carry-the-same-covariance).

### M02 — What a covariance records

- **Central question:** Which state information is retained by first and second moments?
- **Understanding target:** A covariance measures centered fluctuations, while a displacement records first moments. These determine a Gaussian state, but do not determine an arbitrary quantum state.
- **Dependencies and story role:** M01. It turns local observables into the matrix representation used throughout the project.
- **Conceptual connection:** Gaussian dynamics can be solved through matrices; the eventual witness must nevertheless exclude all separable competitors, including non-Gaussian ones.
- **Source pointers:** [W, §II A.1][weedbrook]; [model — Oscillator evolution](../science/model.md#oscillator-evolution); [covariance witnesses — Local covariance constraints](../science/covariance-witnesses.md#local-covariance-constraints).

### M03 — Physical covariance matrices

- **Central question:** Why is a positive real covariance matrix not by itself a quantum state certificate?
- **Understanding target:** The uncertainty condition couples covariance to the commutator matrix. In the project convention it is $V+i\Omega\succeq0$; ordinary matrix positivity alone omits quantum uncertainty.
- **Dependencies and story role:** M01–M02. It adds the physical constraint to the statistical representation.
- **Conceptual connection:** Encoding a target covariance into a dephasing coefficient matrix will work because covariance physicality and generator positivity have matching forms.
- **Source pointers:** [W, §§II A.1 and II C][weedbrook]; [model — Oscillator evolution](../science/model.md#oscillator-evolution); [embedding — Conventions and theorem](../science/reservoir-embedding.md#conventions-and-theorem).

### M04 — Canonical changes of variables

- **Central question:** When does a linear recombination of quadratures describe a physical Gaussian unitary?
- **Understanding target:** A symplectic transformation preserves the full commutator matrix. Squeezing, rotations and beam splitters supply examples; an arbitrary invertible matrix need not preserve canonical structure.
- **Dependencies and story role:** M01–M03. It separates a useful numerical coordinate change from an implementable mode transformation.
- **Conceptual connection:** The extracted target observables require a canonical complement before they can be treated as a subsystem with a local decoder.
- **Source pointers:** [W, §§II A.2, II B.3–4, II B.6 and II C.2][weedbrook]; [embedding — Local canonical extraction and completion](../science/reservoir-embedding.md#local-canonical-extraction-and-completion).

### M05 — Parties, modes and locality

- **Central question:** Which operations are local once modes have been assigned to two parties?
- **Understanding target:** Locality is defined by the selected tensor-product partition. Mixing two modes within one party is local across that partition; a jump combining observables from both parties generally is not.
- **Dependencies and story role:** M01–M04. It assembles modes into a bipartite setting and fixes the meaning of locality before entanglement is discussed.
- **Conceptual connection:** The target, carrier and spin constructions use different numbers of constituents while retaining the same party assignment.
- **Source pointers:** [W, §II D and §II C.2][weedbrook]; [model — Question and conventions](../science/model.md#question-and-conventions); [embedding — Conventions and theorem](../science/reservoir-embedding.md#conventions-and-theorem).

### M06 — Separable mixtures and covariance

- **Central question:** How can a separable state possess correlations without possessing entanglement?
- **Understanding target:** A separable state is a mixture of product states. Its covariance is an average of local covariance blocks plus a positive covariance of the component means, which represents classical correlations.
- **Dependencies and story role:** M02, M03 and M05. It connects the state definition of separability to covariance inequalities.
- **Conceptual connection:** Discarding the positive contribution from fluctuating means gives a lower bound valid against every separable state, rather than only product states.
- **Source pointers:** [W, §II D.1][weedbrook]; [covariance witnesses — Local covariance constraints](../science/covariance-witnesses.md#local-covariance-constraints).

### M07 — Gaussian separability as a matrix condition

- **Central question:** What extra structure makes covariance information sufficient for Gaussian separability?
- **Understanding target:** A Gaussian covariance is separable exactly when it dominates a direct sum of physical local covariances. For a general state, the corresponding covariance condition remains necessary but is not a complete description of its entanglement.
- **Dependencies and story role:** M03, M05 and M06. It turns local uncertainty into a global Gaussian separability criterion.
- **Conceptual connection:** The dominated local covariances later provide local dephasing generators, and the positive remainder provides shared classical phase noise.
- **Source pointers:** [W, §II D.1][weedbrook] for the Gaussian separability setting; [embedding — Separability: both directions](../science/reservoir-embedding.md#separability-both-directions) for the precise Werner–Wolf criterion and its use.

### M08 — Partial transpose in phase space

- **Central question:** How does partial transposition become a covariance test?
- **Understanding target:** Transposition on one party reverses that party's momenta. A Gaussian state is PPT exactly when the transformed covariance still obeys the quantum uncertainty condition.
- **Dependencies and story role:** M03 and M05–M07. It introduces an independently computable entanglement obstruction.
- **Conceptual connection:** The embedding moves the momentum-sign transformation onto the canonical antisymmetric matrix, giving $\Omega_{\mathrm{PT}}=(-\Omega_A)\oplus\Omega_B$ when A is transposed.
- **Source pointers:** [W, §II D.1][weedbrook]; [embedding — Conventions and theorem](../science/reservoir-embedding.md#conventions-and-theorem); [model — A sufficient all-time PPT condition](../science/model.md#a-sufficient-all-time-ppt-condition).

### M09 — PPT, negativity and bound entanglement

- **Central question:** Why can zero negativity coexist with entanglement?
- **Understanding target:** PPT is necessary for separability but is not sufficient for general multimode bipartitions. A PPT-entangled state is nondistillable across that cut. The Gaussian one-mode-versus-many-mode equivalence cannot be applied to a general two-mode-versus-two-mode setting.
- **Dependencies and story role:** M05–M08. It identifies the gap between a partial-transpose test and a full separability decision.
- **Conceptual connection:** The central construction occupies that gap dynamically, so its PPT guarantee and its entanglement certificate must be separate arguments.
- **Source pointers:** [W, §§II D.1–2][weedbrook]; [model — What is conserved and what is supplied](../science/model.md#what-is-conserved-and-what-is-supplied); [Related work](../references/RELATED_WORK.md).

### M10 — A variance witness against all separable states

- **Central question:** How can a few second moments exclude every separable explanation?
- **Understanding target:** A positive weight matrix defines a score whose separable lower bound is the sum of local uncertainty minima. The positive covariance of mixture means cannot lower that score.
- **Dependencies and story role:** M03 and M06–M09. It supplies the second certificate needed when partial transpose remains positive.
- **Conceptual connection:** The project uses this all-state necessity both for Gaussian carriers and, with their actual commutators, for finite spins.
- **Source pointers:** [W, §§II D.1 and II E.1][weedbrook]; [covariance witnesses — The witness bound](../science/covariance-witnesses.md#the-witness-bound) and [Sparse variance witnesses](../science/covariance-witnesses.md#sparse-variance-witnesses).

### M11 — Gaussian channels and their noise

- **Central question:** What allows a linear drift that is not symplectic to define a quantum channel?
- **Understanding target:** A Gaussian channel combines drift and added noise. Complete positivity constrains them together; a reservoir dilation describes the input, interaction and discarded degrees of freedom.
- **Dependencies and story role:** M02–M05. It extends the kinematics of Gaussian unitaries to open-system dynamics.
- **Conceptual connection:** The dephasing drift alone is not a Gaussian unitary. Its diffusion restores complete positivity and identifies where the reservoir's quantum correlations enter.
- **Source pointers:** [W, §V A][weedbrook]; [model — Oscillator evolution](../science/model.md#oscillator-evolution); [embedding — Exact channel and a finite-time dilation](../science/reservoir-embedding.md#exact-channel-and-a-finite-time-dilation).

### M12 — The full reachability question

- **Central question:** What must be shown to establish bound-entanglement creation from a product system state?
- **Understanding target:** The problem requires a well-defined allowed channel, a product input, PPT preservation across a fixed cut and an independent entanglement witness at a finite time. Reservoir resources and the meaning of locality must be included in that statement.
- **Dependencies and story role:** M01–M11. This completes the background phase by assembling the diagnostic tools and physical constraints into one question.
- **Conceptual connection:** Covariance geometry alone establishes possible states; the project asks whether a constrained, population-preserving dynamics can reach them.
- **Source pointers:** [W, §§II D.1–2 and V A][weedbrook]; [scientific overview — How the proofs fit together](../science/README.md#how-the-proofs-fit-together); [model — Question and conventions](../science/model.md#question-and-conventions).

## Phase II — Narrative and innovation: M13–M30

### M13 — The complex dephasing coefficient matrix

- **Central question:** What does the imaginary part of a dephasing coefficient matrix change?
- **Understanding target:** The real symmetric part damps coherences, while the imaginary antisymmetric part contributes a phase coupling between their two eigenvalue labels. Both leave joint dephasing-basis populations fixed. A wholly real coefficient matrix gives a mixture of local phase kicks.
- **Dependencies and story role:** M05, M11 and M12. The narrative starts with the local generator data and its exact action.
- **Conceptual connection:** This separates correlated classical noise from the quantum correlations available to the construction without attributing an extra Hamiltonian to the original generator.
- **Source pointers:** [W, §V A][weedbrook] for channel background; [model — Question and conventions](../science/model.md#question-and-conventions) and [Exact dephasing kernel](../science/model.md#exact-dephasing-kernel) for the project-specific generator.

### M14 — Drift and diffusion from commuting positions

- **Central question:** How can fixed positions coexist with changing correlations and increasing energy?
- **Understanding target:** The oscillator solution has constant position covariance, a position-dependent momentum drift and momentum diffusion. Together these give the stated exact covariance and satisfy the Gaussian complete-positivity condition.
- **Dependencies and story role:** M01–M04, M11 and M13. It turns the kernel into a calculable dynamical model.
- **Conceptual connection:** Dephasing conserves the preferred-basis populations, while the conjugate observables can acquire the correlations needed for a variance-witness violation.
- **Source pointers:** [W, §§II A.1 and V A][weedbrook]; [model — Oscillator evolution](../science/model.md#oscillator-evolution) and [What is conserved and what is supplied](../science/model.md#what-is-conserved-and-what-is-supplied).

### M15 — A generator-level PPT guarantee

- **Central question:** How can PPT be certified for every time without diagonalizing every evolved state?
- **Understanding target:** Conjugating the generator by partial transpose yields a transformed coefficient matrix and, in general, a mathematical Hamiltonian term. Positivity of the transformed coefficient matrix guarantees a completely positive conjugated evolution, hence PPT preservation.
- **Dependencies and story role:** M08–M09 and M13–M14. It supplies the dynamical half of the desired certificate.
- **Conceptual connection:** A property of a small coefficient matrix controls arbitrarily large oscillator or spin Hilbert spaces. This sufficient condition is not asserted as a general separability criterion.
- **Source pointers:** [W, §§II D.1 and V A][weedbrook]; [model — A sufficient all-time PPT condition](../science/model.md#a-sufficient-all-time-ppt-condition).

### M16 — Encoding a target covariance

- **Central question:** Why does $C_G=G-i\Omega$ turn a physical state into a valid dephasing generator?
- **Understanding target:** Complex conjugation transfers covariance physicality to coefficient positivity. There are two carrier oscillators per target mode, and the target canonical form is block diagonal by party.
- **Dependencies and story role:** M03, M05 and M13–M15. It introduces the constructive link between state geometry and dynamics.
- **Conceptual connection:** A target's noncommuting phase-space coordinates label distinct commuting carrier positions; confusing these two roles would miscount both modes and commutators.
- **Source pointers:** [W, §§II A.1, II C and V A][weedbrook]; [embedding — Conventions and theorem](../science/reservoir-embedding.md#conventions-and-theorem).

### M17 — The local reservoir dilation

- **Central question:** Where do the correlations supplied to the carriers physically reside?
- **Understanding target:** A reservoir with covariance $G$ interacts locally with each party's carriers. The exact dilation reproduces the kernel and exposes the reservoir contribution to momentum. Fresh reservoir degrees of freedom are needed when composing time steps.
- **Dependencies and story role:** M05, M11 and M16. It makes the channel's existence and resource accounting explicit.
- **Conceptual connection:** A local interaction can transfer existing bath entanglement into initially uncorrelated carriers. The reduced zero-Hamiltonian statement does not remove the microscopic interaction.
- **Source pointers:** [W, §V A][weedbrook]; [embedding — Exact channel and a finite-time dilation](../science/reservoir-embedding.md#exact-channel-and-a-finite-time-dilation) and [Resources, interpretation, and limitations](../science/reservoir-embedding.md#resources-interpretation-and-limitations).

### M18 — Extracting actual canonical modes

- **Central question:** Why does the extracted observable vector describe a local subsystem?
- **Understanding target:** The vector $X=(P+t\Omega Q)/\sqrt{2t}$ has the target commutators. An explicitly commuting canonical complement completes it to a local symplectic transformation, followed by local discarding.
- **Dependencies and story role:** M04–M05 and M16–M17. It establishes that the target-like covariance belongs to genuine modes.
- **Conceptual connection:** Local extraction cannot create cross-party entanglement; an entangled extracted state therefore certifies entanglement already present in the carrier state.
- **Source pointers:** [W, §§II A.2, II B.3–4, II B.6 and II C.2][weedbrook]; [embedding — Local canonical extraction and completion](../science/reservoir-embedding.md#local-canonical-extraction-and-completion).

### M19 — A finite-time witness survives added noise

- **Central question:** Why does approximate target recovery suffice for an exact entanglement conclusion?
- **Understanding target:** Vacuum input adds $I/(2t)$ to the extracted target covariance. A strict positive witness gap survives whenever its added score is smaller than that gap, yielding a finite sufficient time.
- **Dependencies and story role:** M10 and M16–M18. It turns asymptotically small noise into a finite-time theorem.
- **Conceptual connection:** The argument needs a strict separability-witness violation, not exact recovery of the target or an assertion that entanglement exists only at infinite time.
- **Source pointers:** [W, §§II D.1 and V A][weedbrook]; [embedding — Separability: both directions](../science/reservoir-embedding.md#separability-both-directions).

### M20 — Both directions of separability preservation

- **Central question:** Why does target separability characterize the entangling power of this family exactly?
- **Understanding target:** A separable Gaussian covariance gives local dephasing plus real shared phase noise, or equivalently a separable reservoir in the local dilation. An entangled target has a strict covariance witness whose finite-time extraction contradicts separability preservation.
- **Dependencies and story role:** M06–M07 and M17–M19. It completes the first global correspondence.
- **Conceptual connection:** The forward direction covers arbitrary separable carrier states; a carefully chosen Gaussian product state is enough for the converse. These are different logical tasks.
- **Source pointers:** [W, §§II D.1 and V A][weedbrook]; [embedding — Separability: both directions](../science/reservoir-embedding.md#separability-both-directions), including the covariance-set separation argument.

### M21 — PPT correspondence and fixed-time quantifiers

- **Central question:** Which state and channel statements are equivalent, and what resources enter their converses?
- **Understanding target:** Target PPT is equivalent to all-time PPT preservation in the encoded family. A non-PPT target remains non-PPT after sufficiently small added noise. Finite independent input squeezing supplies the analogous converse at any fixed positive time.
- **Dependencies and story role:** M08–M09, M15 and M18–M20. It combines the two correspondences into the general PPT-entangling construction.
- **Conceptual connection:** The universal statement concerns this encoded family. Vacuum at sufficiently large time and squeezed input at a prescribed time have distinct resource assumptions.
- **Source pointers:** [W, §§II B.3, II D.1 and V A][weedbrook]; [embedding — Conventions and theorem](../science/reservoir-embedding.md#conventions-and-theorem) and [PPT: exact covariance-to-generator correspondence](../science/reservoir-embedding.md#ppt-exact-covariance-to-generator-correspondence).

### M22 — A concrete physical and PPT target

- **Central question:** What exact data instantiate the general construction?
- **Understanding target:** The inherited Werner–Wolf four-mode covariance has explicitly nonnegative physicality and partial-transpose uncertainty spectra. Adding $I/30$ supplies strict margins; encoding it requires eight carrier modes, four per party.
- **Dependencies and story role:** M03, M08 and M16–M21. It converts the theorem's abstract target into fully specified data.
- **Conceptual connection:** The integer target is an established Gaussian bound-entangled example. The new use is its realization within the restricted dephasing dynamics.
- **Source pointers:** [W, §§II C and II D.1][weedbrook]; [embedding — An explicit integer example](../science/reservoir-embedding.md#an-explicit-integer-example); [bridge — A complete eight-carrier example](WEEDBROOK_BRIDGE.md#a-complete-eight-carrier-example).

### M23 — Four variances certify the example

- **Central question:** How does the exact benchmark produce an observable separability violation?
- **Understanding target:** Four doubled variances have separable lower bound 28 and target score 26. Added target noise and finite-time extraction give $26+30\delta+15/t$, equal to $55/2$ at $\delta=1/30$, $t=30$.
- **Dependencies and story role:** M10, M18–M19 and M22. It completes the input–channel–measurement–conclusion chain for one example.
- **Conceptual connection:** The variance score is evaluated after local decoding or through its pullback to carrier observables. Incompatible quadratures use separate preparations; no outcome postselection generates the certified state.
- **Source pointers:** [W, §§II D.1 and II E.1][weedbrook]; [embedding — An explicit integer example](../science/reservoir-embedding.md#an-explicit-integer-example); [covariance witnesses — Sparse variance witnesses](../science/covariance-witnesses.md#sparse-variance-witnesses).

### M24 — A smaller carrier certificate

- **Central question:** How does the four-carrier construction differ from the eight-carrier encoding example?
- **Understanding target:** The smaller construction directly specifies rational coefficient and witness matrices. Exact positive minors and radical bounds separately establish physicality, all-time PPT and a strict oscillator witness gap at $t=28/5$.
- **Dependencies and story role:** M10, M14–M15 and M23. It supplies the particular data used for the smaller finite-qubit realization.
- **Conceptual connection:** A transparent general mechanism and a compact explicit example serve different purposes. Neither carrier count is an optimality theorem.
- **Source pointers:** [W, §§II C and II D.1][weedbrook]; [four-mode certificate — The coefficient matrix](../science/four-mode-certificate.md#the-coefficient-matrix), [Exact physicality and all-time PPT](../science/four-mode-certificate.md#exact-physicality-and-all-time-ppt) and [Entanglement of the oscillator output](../science/four-mode-certificate.md#entanglement-of-the-oscillator-output).

### M25 — Finite ensembles are not exact oscillators

- **Central question:** What changes when a carrier mode is replaced by finitely many qubits?
- **Understanding target:** Normalized collective $Z$ and $Y$ components reproduce vacuum-like initial second moments, but their commutator contains the operator $\overline X_j$. The same coefficient positivity conditions still apply to these bounded commuting dephasing observables.
- **Dependencies and story role:** M01, M13, M15 and M24. It opens the finite-dimensional construction without assuming an oscillator approximation as a proof.
- **Conceptual connection:** The boson–ensemble correspondence motivates the choice; the actual finite-spin commutators determine what must be certified.
- **Source pointers:** [W, §§II A and II B.1][weedbrook] for the oscillator reference; [finite-spin transfer — Statement of the transfer theorem](../science/finite-spin-transfer.md#1-statement-of-the-transfer-theorem) and [Physicality and PPT are uniform in the group size](../science/finite-spin-transfer.md#2-physicality-and-ppt-are-uniform-in-the-group-size).

### M26 — Exact moments and the moving threshold

- **Central question:** How is entanglement tested without constructing the full many-qubit density matrix?
- **Understanding target:** The dephasing kernel yields exact Pauli moments through spin flips and averages over the product input. The separability threshold uses magnetizations of that same evolved state, because they enter its commutator matrix.
- **Dependencies and story role:** M06, M10, M13 and M25. It gives a finite-spin test with no Gaussian-state assumption.
- **Conceptual connection:** Both the witness score and its threshold change with group size. Comparing only the score to the canonical oscillator bound would leave a gap.
- **Source pointers:** [W, §§II A.1 and II D.1][weedbrook] for the moment and separability background; [finite-spin transfer — Exact finite-spin moments](../science/finite-spin-transfer.md#3-exact-finite-spin-moments) and [The finite-spin separability threshold](../science/finite-spin-transfer.md#4-the-finite-spin-separability-threshold).

### M27 — From a strict oscillator gap to finite qubits

- **Central question:** What turns a limiting resemblance into a theorem at finite group size?
- **Understanding target:** Explicit decreasing bounds control the covariance-score error and the loss of the spin separability threshold. Their sum eventually falls below the strict oscillator gap, certifying every larger integer group size.
- **Dependencies and story role:** M19, M24–M26. It proves a reusable transfer theorem rather than just one numerical instance.
- **Conceptual connection:** Convergence of the witness and its state-dependent threshold is sufficient. No trace-norm convergence across changing Hilbert spaces or exact spin decoder is required.
- **Source pointers:** [W, §§II A.1 and II D.1][weedbrook] for the limiting covariance framework; [finite-spin transfer — Explicit convergence and a sufficient finite size](../science/finite-spin-transfer.md#5-explicit-convergence-and-a-sufficient-finite-size), especially [Witness error and threshold loss](../science/finite-spin-transfer.md#witness-error-and-threshold-loss).

### M28 — What the finite-size certificates establish

- **Central question:** Why are the direct certificate and the general size bound different numbers?
- **Understanding target:** Exact interval evaluation certifies four groups of 512 qubits, while the deliberately conservative general estimate gives 16,384 per group for those data. The separate eight-group lift is another realization. Rational outward intervals decide the strict gaps.
- **Dependencies and story role:** M24–M27. It connects the theorem to actual finite-dimensional output states and reproducible evidence.
- **Conceptual connection:** A sufficient analytic size, a sharper direct instance and a minimum possible size are distinct claims; only the first two are supplied.
- **Source pointers:** [W, §II D.1][weedbrook] for the separability distinction; [four-mode certificate — An exact finite-qubit realization](../science/four-mode-certificate.md#an-exact-finite-qubit-realization); [finite-spin transfer — Exact finite constructions](../science/finite-spin-transfer.md#6-exact-finite-constructions); [verification guide](../verification/README.md#exact-inputs-and-numerical-decisions).

### M29 — A nonzero region of valid generators

- **Central question:** Does the finite-qubit conclusion survive specified perturbations without retuning the witness?
- **Understanding target:** Exact positivity margins and parameter intervals preserve both PPT and a strict witness gap throughout the stated coefficient box, and separately under added local group dephasing. These are uniform guarantees for two distinct perturbation families.
- **Dependencies and story role:** M15 and M24–M28. It expands one finite instance into a controlled neighborhood while preserving the model assumptions.
- **Conceptual connection:** Robustness of the theorem's generator parameters is different from tolerance to independent noise on every qubit, state-preparation error or arbitrary laboratory imperfections.
- **Source pointers:** [W, §§II D.1 and V A][weedbrook]; [robustness — Independent coefficient perturbations](../science/robustness.md#independent-coefficient-perturbations), [Added local group dephasing](../science/robustness.md#added-local-group-dephasing) and [Verification and interpretation](../science/robustness.md#verification-and-interpretation).

### M30 — The complete physical and mathematical claim

- **Central question:** What has been established once the mechanism, certificates and resources are considered together?
- **Understanding target:** Quantum-correlated noise can transfer entanglement into individually uncorrelated systems through Hamiltonian-free pure dephasing while preserving PPT across a fixed cut. The result includes an exact Gaussian correspondence, finite-time examples and genuine finite-qubit witnesses, with explicit reservoir, decoding, energy and robustness qualifications.
- **Dependencies and story role:** M12–M29. This completes the narrative phase by joining the general theorem, smaller construction, finite-spin proof and bounded physical interpretation.
- **Conceptual connection:** The scientific addition is the constrained dynamical realization and correspondence. Gaussian bound entanglement, reservoir transfer and boson–spin mappings retain their established attributions.
- **Source pointers:** [W, §§II D.1–2 and V A][weedbrook]; [scientific overview — How the proofs fit together](../science/README.md#how-the-proofs-fit-together); [embedding — Resources, interpretation, and limitations](../science/reservoir-embedding.md#resources-interpretation-and-limitations); [Related work](../references/RELATED_WORK.md); [bridge — From the example to the full result](WEEDBROOK_BRIDGE.md#from-the-example-to-the-full-result).

[weedbrook]: https://arxiv.org/abs/1110.3234v1
