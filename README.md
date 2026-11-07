# Pure Dephasing Bound Entanglement

**Pure Markovian dephasing can create bound entanglement from a fully product system state.** The dynamics have zero system Hamiltonian and preserve positive partial transpose (PPT) across a specified bipartition at every time, while a separate witness proves that the output becomes entangled across that same partition.

The central mechanism encodes a Gaussian covariance in the correlations of a dephasing reservoir. Its separability and PPT properties become corresponding properties of the induced dephasing channels. An exact collective-spin transfer theorem then gives finite-dimensional realizations, including a certified example with **2,048 individually unentangled input qubits**.

## Principal results

| Result | Established statement | Authoritative account |
|---|---|---|
| Gaussian covariance encoding | A target with r modes defines pure dephasing on 2r carrier oscillators. Local extraction returns the target covariance plus explicitly known additive noise. | [Reservoir embedding](science/reservoir-embedding.md) |
| Exact correspondence | Within this family, separability preservation is equivalent to target Gaussian separability, and PPT preservation is equivalent to target PPT. | [The theorem and its proof](science/reservoir-embedding.md) |
| Transparent example | A known integer Gaussian bound-entangled covariance yields eight vacuum carriers with an exact witness score of 27.5 below the separable bound of 28. | [Integer construction](science/reservoir-embedding.md#an-explicit-integer-example) |
| Smaller explicit realization | A rational four-carrier construction transfers to 2,048 qubits, with a rigorously certified witness gap greater than 0.01193862775480. | [Four-mode and qubit certificate](science/four-mode-certificate.md) |
| Finite-size control | Explicit error bounds transfer every strict vacuum covariance witness at a fixed time to sufficiently large finite spin groups. | [Finite-spin transfer](science/finite-spin-transfer.md) |
| Parameter stability | The 2,048-qubit witness survives a specified coefficient-error box and, separately, a range of added group dephasing. | [Robustness](science/robustness.md) |

## Read the science

Start with [the scientific overview](science/README.md). The [model](science/model.md) fixes the pure-dephasing convention and the selected-cut PPT condition. The [reservoir embedding](science/reservoir-embedding.md) explains why bound entanglement can appear. The [covariance-witness proof](science/covariance-witnesses.md) applies to arbitrary separable states, and the [finite-spin theorem](science/finite-spin-transfer.md) treats the actual spin commutators.

The [related-work account](references/RELATED_WORK.md) identifies the inherited Gaussian covariance criteria, reservoir-transfer methods and partial-transpose generator test. The added conclusion concerns the restricted, time-homogeneous, commuting-observable pure-dephasing class. Gaussian bound entanglement, reservoir entanglement transfer and general PPT-preserving entangling channels were already known.

## Learn the project

The educational anchor is **Weedbrook et al., _Gaussian Quantum Information_**, Reviews of Modern Physics 84, 621–669 (2012), using the openly available [arXiv:1110.3234v1 author version](https://arxiv.org/abs/1110.3234v1) for section references. The [Weedbrook bridge](learning/WEEDBROOK_BRIDGE.md) translates the quadrature conventions and connects Gaussian-state geometry to the dephasing channel, local extraction and exact finite-spin witness.

The [30-milestone map](learning/MILESTONES.md) has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The first phase builds the state, channel and covariance framework; the second assembles the mechanism, finite examples, transfer proof and robustness into the complete result. Each milestone identifies a central question, understanding target, dependencies, conceptual connection and scientific sources.

Use the bridge alongside the map, or follow the direct scientific route above. The [LLM reading guide](llms.txt) maps questions to the authoritative proofs, learning material and reproduction commands.

## Reproduce the certificates

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_transduction.py
python verification/independent_dephasing_certificate.py
python verification/finite_spin_bounds.py
python verification/finite_spin_intervals.py
python verification/robustness_certificate.py
```

The [verification guide](verification/README.md) gives the expected outputs and proof scope. Exact minors, symbolic identities and outward-rounded rational intervals determine the reported certificates; numerical optimization is not needed to reproduce them.

## Physical scope

The system input is a product state. Quantum-correlated reservoir noise supplies the entanglement resource. The original reduced generator contains no Hamiltonian, monitoring or postselection, while a microscopic dilation uses ordinary local system–reservoir interactions. Its collective Lindblad jumps are not independent classical phase noise.

The PPT guarantee is for the stated bipartition. Oscillator position dephasing can increase energy. Local decoding is only a proof device for certifying entanglement of the carrier output; implementing target-state extraction additionally requires the stated local operations. Neither the oscillator nor finite-qubit counts are an experimental optimum, and no minimum qubit count is claimed.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
