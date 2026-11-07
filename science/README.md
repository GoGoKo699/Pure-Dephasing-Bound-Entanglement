# Scientific overview

[Repository](../README.md) · [Related work](../references/RELATED_WORK.md) · [Verification](../verification/README.md)

Dephasing fixes populations in a preferred basis. Real correlated phase noise acts as a mixture of local phase rotations, so it cannot create entanglement from a separable input. Complex quantum correlations in a Markovian dephasing reservoir allow a different behavior: the output can become entangled even while partial transposition remains positive throughout the evolution.

The key result is a constructive separation **inside pure dephasing**. It uses zero system Hamiltonian, a fixed time-independent generator, commuting system observables and a fully product system input. A fixed bipartition is used both for the all-time PPT guarantee and for the entanglement witness. The finite-qubit realization proves the effect in a bounded, finite-dimensional model.

## Connected reading route

1. [Model and partial transpose](model.md): the exact dephasing kernel, the transformed generator, and the oscillator channel.
2. [Reservoir embedding](reservoir-embedding.md): encode any Gaussian covariance into pure dephasing, extract its correlations locally, and prove the separability/PPT correspondences. A sparse integer example makes the mechanism explicit.
3. [Covariance witnesses](covariance-witnesses.md): derive a bound valid for every separable state, including non-Gaussian states and finite-spin groups.
4. [Four-mode certificate](four-mode-certificate.md): an exact rational example with a smaller carrier count and a 2,048-qubit realization.
5. [Finite-spin transfer](finite-spin-transfer.md): exact Pauli moments, quantitative convergence and a computable finite-size criterion.
6. [Robustness](robustness.md): uniform certificates over coefficient perturbations and added local group-dephasing rates.

## How the proofs fit together

For the general construction, a centered Gaussian reservoir covariance G determines the coefficient matrix C = G − iΩ. An explicit local dilation shows that this is pure dephasing and exposes a local subsystem with covariance G + I/(2t) for vacuum carrier input. A strict target covariance witness therefore detects entanglement at a finite time. Separable reservoir covariances give separability-preserving channels; a PPT reservoir gives a completely PPT-preserving channel. The local extraction proves the converse directions.

For finite spins, the same coefficient matrix acts on normalized collective Z observables. Its complete-positivity and PPT certificates are unchanged. Exact finite-size moments converge to the oscillator moments, while the state-dependent separability threshold converges to its canonical value. A strict witness violation thus survives at finite group size. The explicit 2,048-qubit result is established directly by rational intervals and is sharper than the general sufficient-size estimate.

The quantum reservoir is the source of the transferred correlations. The result does not assert entanglement creation by local classical noise or from a globally uncorrelated system-plus-environment state. The [resource discussion](reservoir-embedding.md) charges the reservoir, finite-time noise, local decoding and energy growth.

## Scientific position

The underlying correlated-dephasing model and partial-transpose test come from Seif, Wang and Clerk. Gaussian covariance separability and the integer bound-entangled target come from Werner and Wolf. General Gaussian reservoir transfer and PPT-preserving entangling Gaussian channels have separate precedents. [The comparison](../references/RELATED_WORK.md) explains why those results do not already state the same commuting-position dephasing construction and finite-spin certificate.
