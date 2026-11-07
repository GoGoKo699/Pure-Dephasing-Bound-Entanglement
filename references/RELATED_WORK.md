# Related work and scientific scope

[Scientific route](../science/README.md) · [BibTeX references](references.bib)

This repository establishes finite-time creation of positive-partial-transpose (PPT) entanglement by a restricted Markovian dynamics: the system Hamiltonian vanishes, every jump is a linear combination of mutually commuting dephasing observables, and the system starts in a product state over its individual constituents. The bipartition is fixed throughout each claim. The [Gaussian embedding](../science/reservoir-embedding.md) gives a general correspondence between Gaussian state separability and the entangling power of this dephasing family. The [four-mode certificate](../science/four-mode-certificate.md) and [finite-spin transfer](../science/finite-spin-transfer.md) give explicit instances. The distinctions from prior work concern these dynamical restrictions and certificates; the covariance criteria and the existence of Gaussian bound entanglement have established precedents.

[Michał, Paweł and Ryszard Horodecki (1998)](https://doi.org/10.1103/PhysRevLett.80.5239) establish that distillation to singlet entanglement requires violation of the partial-transpose criterion. Consequently, an entangled state that remains PPT is nondistillable by local operations and classical communication across that partition. This established implication is what justifies the term *bound entanglement* after the separate PPT and entanglement certificates in this repository.

## Correlated dephasing and the open question

[Seif, Wang and Clerk (2022)](https://doi.org/10.1103/PhysRevLett.128.070402) study correlated Markovian dephasing of qubits, with complex positive coefficient matrices and no system Hamiltonian in the dephasing problem. They derive a partial-transpose test for dissipative entangling power and explain the role of quantum noise correlations. Their Eq. (4) and the accompanying discussion supply the transformed coefficient matrix used in [our model](../science/model.md). They explicitly recognize that a negativity-based test does not settle PPT entanglement in larger systems. The present construction uses the positive transformed-generator condition to guarantee PPT at every time, then establishes entanglement by an independent separability witness. It therefore completes a case left undecided by that sufficient entanglement test.

[Wang's dissertation (2023)](https://knowledge.uchicago.edu/records/0m9cq-pyy36), Sec. 2.5, printed p. 18, explicitly asks whether pure-dephasing dynamics can create bound entanglement and reports neither an example nor a general exclusion theorem. The present product-input constructions answer that reachability question. The dissertation also treats more general multipartite dephasing observables; the question is broader than the original qubit presentation.

[Seif, Wang, Movassagh and Clerk (2024)](https://doi.org/10.1103/PhysRevLett.133.050402) subsequently analyze entanglement-negativity transitions for random commuting measurement-and-feedforward processes and their relation to correlated dephasing. Their framework includes a commuting-quadrature bosonic extension. The PPT-entangling sector considered here is compatible with a transition formulated in terms of negativity: a PPT-entangled output has zero negativity across the selected cut. The construction does not establish invisibility to negativity tests across every other partition.

## Gaussian covariances and reservoir transfer

### Covariance and witness provenance

[Werner and Wolf (2001)](https://doi.org/10.1103/PhysRevLett.86.3658) establish the covariance characterization of Gaussian separability and exhibit Gaussian PPT-entangled states with two modes per party. In the doubled-covariance convention used here, a Gaussian covariance is separable exactly when it dominates a direct sum of physical local covariances. The integer covariance $G_0$ used in [the eight-carrier example](../science/reservoir-embedding.md#an-explicit-integer-example) is their Eq. (9), with the coordinate ordering stated explicitly in our derivation. It is an inherited bound-entangled state, subsequently encoded into a dephasing generator.

[Hyllus and Eisert (2006)](https://doi.org/10.1088/1367-2630/8/4/051) develop linear second-moment entanglement witnesses, their optimization by semidefinite programming, and their applicability to non-Gaussian states. Our [covariance-witness proof](../science/covariance-witnesses.md) states the required uncertainty bound directly. The finite-spin application retains the actual state-dependent spin commutators, so its separability test does not assume a Gaussian state or replace finite spins by exact canonical variables.

[Wang, Seif and Clerk (2024)](https://doi.org/10.1103/PhysRevA.110.L050602), in their discussion of many-body extensions, already use the Holstein–Primakoff correspondence to replace each bosonic mode by an ensemble of $2S$ spins, with a quadrature mapped to a rescaled collective spin component $S_x/\sqrt S$. That boson-to-ensemble correspondence is established. The additional result in [our finite-spin construction](../science/finite-spin-transfer.md) is a rigorous finite-size PPT-entanglement certificate using exact moments and the actual spin commutators.

### Hamiltonian-free dissipative transfer

[Yamamoto (2012)](https://doi.org/10.1098/rsta.2011.0529), Sec. IV and Proposition 4, already formulates Gaussian input-field-to-memory transfer by dissipative dynamics. In the universal pure-state-transfer setting analyzed there, the memory has zero system Hamiltonian and obeys a damping equation. Its reservoir couplings involve general canonical quadratures. Thus Gaussian reservoir transfer, including a zero system Hamiltonian, is established. The additional restriction here is that all carrier positions are conserved and all system jump operators belong to their commuting algebra. Ordinary damping and the associated annihilation-type couplings do not have that property.

### PPT-preserving Gaussian channels with entangling power

[Rau et al. (2022)](https://doi.org/10.1103/PhysRevApplied.17.044057), Sec. IV A and Eqs. (6) and (8), identify a region of a doubly parametric Gaussian transducer that is inseparable yet PPT preserving. They explain how local ancillary entanglement on each side reveals its capacity to generate Gaussian bound entanglement. This is a direct precedent for physical Gaussian channels that preserve PPT while creating entanglement. Their transducer uses coherently driven interactions and losses; it is not the population-preserving, Hamiltonian-free dephasing semigroup considered here. Our product-vacuum construction also supplies an explicit input without initial entanglement among the carrier modes within either party. The [open author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC9830939/) gives the channel model and these distinctions in full.

### Quantum-nondemolition interfaces

[Marek and Filip (2010)](https://doi.org/10.1103/PhysRevA.81.042325), Secs. II–III, construct a quantum interface from two quantum-nondemolition (QND) interactions. Their deterministic transfer uses optical preprocessing, homodyne measurements and displacement feedforward; a probabilistic alternative trades feedforward for postselection. This is an established precedent for state transfer using restricted couplings. The present reduced dynamics instead forms one unconditional, time-homogeneous dephasing semigroup. Its finite-time local dilation also has a QND interpretation, but no measurement record or postselection enters the reduced channel. A local decoder is used to identify the recovered canonical subsystem, and its resources are stated explicitly.

## Other bound-entangled preparations and noisy trajectories

[Ma, Woolley, Jia and Zhang (2019)](https://doi.org/10.1103/PhysRevA.100.022309) propose optical preparation of Gaussian bound entanglement using vacuum and thermal inputs, interferometers and squeezing. This establishes a preparation route for the state class; it does not impose a pure-dephasing generator or a PPT-preserving semigroup at every time.

[Thomas, Bohmann and Vogel (2017)](https://doi.org/10.1103/PhysRevA.96.042321) verify bound entanglement of dephased qutrit Werner states. [Singh, Roy and Arvind (2025)](https://doi.org/10.1103/vpq9-691b) exhibit a transient Gaussian bound-entangled phase as initially NPT-entangled states evolve under thermal noise. These results concern the conversion or persistence of entanglement already present in the initial state. The construction here starts with an individually factorized system state and remains PPT across the specified cut throughout its evolution.

## Precise contribution and resource accounting

The [embedding theorem](../science/reservoir-embedding.md) associates a physical $r$-mode Gaussian covariance $G$ with a dephasing coefficient matrix

$$
C_G=G-i\Omega
$$

on $2r$ carrier oscillators, where the canonical antisymmetric matrix $\Omega$ is block diagonal by party. A local canonical extraction from the evolved product vacuum has covariance $G+I/(2t)$. Gaussian separability is equivalent to separability preservation by every channel in this semigroup; Gaussian PPT is equivalent to PPT preservation at every time. An entangled target is therefore witnessed after a sufficiently large finite time, and a PPT-entangled target gives a PPT-entangling dephaser. The theorem also states the fixed-time correspondences when finite independent input squeezing is allowed. The result is this correspondence inside the restricted dephasing class, together with explicit finite-time and finite-spin certificates.

The bath correlations are a supplied resource. In the local dilation, the reservoir itself has covariance $G$; an entangled target therefore uses an entangled reservoir. A realization based instead on independent vacuum reservoirs would require collective coupling operators. The absence of a system Hamiltonian in the reduced generator does not remove the interaction Hamiltonian needed in a microscopic dilation. The per-time dilation uses fresh reservoir degrees of freedom when channels are composed, rather than asserting a semigroup from repeatedly using one finite bath.

At finite time, the extracted state contains the explicit additive noise $I/(2t)$. Physical target-state recovery includes local squeezing, rotations and mode mixing in the decoder. Entanglement certification can instead use the corresponding pulled-back variance witness without implementing that decoder. The examples make no minimum-system-size or experimental-resource optimum claim. Their PPT statements apply to the designated bipartition, not automatically to every cut.

## Bibliographic entries

The citation keys below match [references.bib](references.bib).

1. **SeifWangClerk2022.** A. Seif, Yu-Xin Wang and A. A. Clerk, “Distinguishing between Quantum and Classical Markovian Dephasing Dissipation,” *Physical Review Letters* **128**, 070402 (2022). [DOI](https://doi.org/10.1103/PhysRevLett.128.070402) · [arXiv:2109.06155](https://arxiv.org/abs/2109.06155).

2. **Wang2023Thesis.** Yuxin Wang, *Noise and Fluctuations for Quantum Information Processing*, Ph.D. dissertation, University of Chicago (August 2023), Sec. 2.5, p. 18. [DOI](https://doi.org/10.6082/uchicago.7538) · [Repository and PDF](https://knowledge.uchicago.edu/records/0m9cq-pyy36).

3. **SeifEtAl2024.** A. Seif, Yu-Xin Wang, R. Movassagh and A. A. Clerk, “Measurement and Feed Forward Induced Entanglement Negativity Transition,” *Physical Review Letters* **133**, 050402 (2024). [DOI](https://doi.org/10.1103/PhysRevLett.133.050402) · [arXiv:2310.18305](https://arxiv.org/abs/2310.18305).

4. **WernerWolf2001.** R. F. Werner and M. M. Wolf, “Bound Entangled Gaussian States,” *Physical Review Letters* **86**, 3658–3661 (2001). [DOI](https://doi.org/10.1103/PhysRevLett.86.3658) · [arXiv:quant-ph/0009118](https://arxiv.org/abs/quant-ph/0009118).

5. **HyllusEisert2006.** P. Hyllus and J. Eisert, “Optimal entanglement witnesses for continuous-variable systems,” *New Journal of Physics* **8**, 51 (2006). [DOI](https://doi.org/10.1088/1367-2630/8/4/051) · [arXiv:quant-ph/0510077](https://arxiv.org/abs/quant-ph/0510077).

6. **Yamamoto2012.** N. Yamamoto, “Pure Gaussian state generation via dissipation: A quantum stochastic differential equation approach,” *Philosophical Transactions of the Royal Society A* **370**, 5324–5337 (2012). [DOI](https://doi.org/10.1098/rsta.2011.0529) · [arXiv:1112.5889](https://arxiv.org/abs/1112.5889).

7. **RauEtAl2022.** C. L. Rau, A. Kyle, A. Kwiatkowski, E. Shojaee, J. D. Teufel, K. W. Lehnert and T. Dennis, “Entanglement Thresholds of Doubly Parametric Quantum Transducers,” *Physical Review Applied* **17**, 044057 (2022). [DOI](https://doi.org/10.1103/PhysRevApplied.17.044057) · [arXiv:2110.10235](https://arxiv.org/abs/2110.10235).

8. **MarekFilip2010.** P. Marek and R. Filip, “Noise-resilient quantum interface based on quantum nondemolition interactions,” *Physical Review A* **81**, 042325 (2010). [DOI](https://doi.org/10.1103/PhysRevA.81.042325) · [arXiv:1002.0225](https://arxiv.org/abs/1002.0225).

9. **MaEtAl2019.** S. Ma, M. J. Woolley, X. Jia and J. Zhang, “Preparation of bipartite bound entangled Gaussian states in quantum optics,” *Physical Review A* **100**, 022309 (2019). [DOI](https://doi.org/10.1103/PhysRevA.100.022309) · [arXiv:1904.11748](https://arxiv.org/abs/1904.11748).

10. **ThomasEtAl2017.** P. Thomas, M. Bohmann and W. Vogel, “Verifying bound entanglement of dephased Werner states,” *Physical Review A* **96**, 042321 (2017). [DOI](https://doi.org/10.1103/PhysRevA.96.042321) · [arXiv:1708.03109](https://arxiv.org/abs/1708.03109).

11. **SinghEtAl2025.** G. Singh, S. Roy and Arvind, “Noisy dynamics of Gaussian entanglement: A transient bound entangled phase before separability,” *Physical Review A* **112**, 052424 (2025). [DOI](https://doi.org/10.1103/vpq9-691b) · [arXiv:2503.12694](https://arxiv.org/abs/2503.12694).

12. **WangSeifClerk2024.** Yu-Xin Wang, A. Seif and A. A. Clerk, “Uncovering measurement-induced entanglement via directional adaptive dynamics and incomplete information,” *Physical Review A* **110**, L050602 (2024). [DOI](https://doi.org/10.1103/PhysRevA.110.L050602) · [arXiv:2310.01338](https://arxiv.org/abs/2310.01338).

13. **HorodeckiEtAl1998.** M. Horodecki, P. Horodecki and R. Horodecki, “Mixed-state entanglement and distillation: Is there a ‘bound’ entanglement in nature?”, *Physical Review Letters* **80**, 5239–5242 (1998). [DOI](https://doi.org/10.1103/PhysRevLett.80.5239) · [arXiv:quant-ph/9801069](https://arxiv.org/abs/quant-ph/9801069).
