# Reproducing the scientific certificates

[Scientific overview](../science/README.md)

The exact checks require Python 3.10 or newer and SymPy. They were run with Python 3.12.3 and SymPy 1.14.0. Run from the repository root, without Python optimization (`-O`). The decisive programs reject optimized execution so their assertions cannot be silently removed.

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_transduction.py
python verification/independent_dephasing_certificate.py
python verification/finite_spin_bounds.py
python verification/finite_spin_intervals.py
python verification/robustness_certificate.py
```

Each command writes the corresponding JSON output next to its source. The committed outputs are reproducible records, rather than substitutes for running the commands.

| Program | What it checks | Expected decisive result |
|---|---|---|
| [verify_transduction.py](verify_transduction.py) | Symbolic CCR, local canonical completion, extracted covariance, dilation covariance, PPT congruence and the integer example | Score 55/2 below 28 at noise 1/30 and time 30 |
| [independent_dephasing_certificate.py](independent_dephasing_certificate.py) | Rational positivity of C, its transpose coefficient matrix and W; oscillator radical bound; exact finite-spin witness | 2,048-qubit gap greater than 0.01193862775480 |
| [finite_spin_bounds.py](finite_spin_bounds.py) | Rational evaluation of the general sufficient-size error bounds | Conservative m = 16,384; this does not replace the sharper m = 512 exact certificate |
| [finite_spin_intervals.py](finite_spin_intervals.py) | Exact moments and state-dependent variance witness for the integer target's eight-group spin realization | A positive certified gap at m = 16,384, or 131,072 qubits |
| [robustness_certificate.py](robustness_certificate.py) | Exact shifted positivity and interval bounds uniform over parameter sets | Positive gaps for the stated coefficient box and separately for added group dephasing |

## Exact inputs and numerical decisions

[gaussian_exact_certificate.json](gaussian_exact_certificate.json) contains the exact integer matrices and denominators for the four-group construction, its rational time, and its local radical invariants. The script reconstructs its determinant and witness claims from those inputs. [transduction_verification.json](transduction_verification.json) records the integer target covariance, sparse witness factor and symbolic construction checks.

The finite-spin arithmetic uses rational endpoints rounded outward to denominator 10^50. Exponential, sine and cosine values are bounded by adjacent alternating Taylor sums, with the required argument domains explicitly checked. Integer powers, products, division and square roots are enclosed outward. Float conversions are used only for readable output; they do not decide positivity or witness violation.

Parameter robustness uses interval-valued generator coefficients and the same exact moment formulas. This encloses every parameter choice in the specified box, rather than testing a finite sample. The positivity margin is established independently by exact shifted principal minors.

## What these checks establish

The scripts verify the explicit algebra and instances accompanying the proofs. The general Gaussian encoding theorem and the finite-spin transfer theorem are proved in the scientific pages; checking matrices for one mode count does not by itself prove arbitrary-dimensional statements. Likewise, an exact example is not a minimum-size theorem or an experimental feasibility demonstration.

The finite-spin certificate uses the actual magnetization-dependent commutators. It applies to all separable states across the chosen parties, including states with arbitrary internal entanglement within a party. No matrix of size 2 to the power of the total qubit count is constructed.

## Regenerate the analytic figure

```bash
python -m pip install -r verification/requirements-figures.txt
python verification/plot_witness_region.py
```

The plot shows only the sufficient entanglement region of the displayed sparse witness. The unshaded area is not asserted to be separable. It is generated directly from the analytic inequality and is not a new numerical experiment.
