# Quantified robustness of the finite-qubit construction

[Scientific route](README.md) · [Four-mode coefficient matrix](four-mode-certificate.md) · [Exact finite-spin moments](finite-spin-transfer.md)

The 2,048-qubit example occupies a nonzero region of the ideal dephasing-generator parameter space. Fix the four-group matrices $R$ and $B$ from the explicit construction, the time $t=28/5$, the group size $m=512$ and its rational witness $W$. Below, $B_0$ is that real antisymmetric matrix and $C^\Gamma$ is the same transformed coefficient matrix denoted $C_T$ in the model page.


The same fixed time $t=28/5$ and fixed rational witness work in two nonzero parameter neighborhoods.

### Independent coefficient perturbations

Let $C'=R'+iB_0'$, where $R'$ remains real symmetric and $B_0'$ real antisymmetric. Allow every independent entry of $R'$ to vary within $10^{-4}$ of its stated value and every independent off-diagonal entry of $B_0'$ within $10^{-4}$; its diagonal remains zero.

Exact principal minors prove

$$
C-\frac1{500}I>0,\qquad
C^\Gamma-\frac1{250}I>0.
$$

There are four real diagonal entries and six complex off-diagonal pairs, so
$\|C'-C\|_{\mathrm{op}}\le\sqrt{28}\,10^{-4}<6\,10^{-4}$.
The linear coefficient transformation obeys
$\|(C')^\Gamma-C^\Gamma\|_{\mathrm{op}}\le2\|C'-C\|_{\mathrm{op}}$.
Thus complete positivity and all-time PPT preservation hold throughout this box.

Interval evaluation of the exact moments and state-dependent witness threshold uniformly over the whole box certifies

$$
b_m-\operatorname{Tr}(W V_m)>0.00911117269.
$$

The interval treatment permits dependencies among entries; forgetting those dependencies only enlarges the enclosure and cannot invalidate the guarantee.

### Added local group dephasing

Independently add diagonal rates $d_j\in[0,1/200]$ to $R$, with $B_0$ unchanged. This adds
$\sum_jd_j\mathcal D[Q_j^{(m)}]$, an uncorrelated local dephasing term for each group. It preserves positivity of both coefficient matrices automatically.

At $m=512$, the exact interval certificate uniformly gives

$$
b_m-\operatorname{Tr}(W V_m)>0.00127134452.
$$

These statements quantify robustness within the stated ideal generator model. They do not describe tolerance to arbitrary gate errors, finite detector resolution, independent dephasing of every physical qubit, or errors in preparing the initial product state.


## Verification and interpretation

[robustness_certificate.py](../verification/robustness_certificate.py) reconstructs the shifted principal minors and encloses the exact finite-spin moments for every parameter in each stated range. Its [recorded rational intervals](../verification/robustness_certificate.json) include the score, separability threshold and gap. No random parameter sampling enters either guarantee.

The two families are separate sufficient guarantees; their maximum perturbations are not asserted to hold simultaneously. The bounds apply to the fixed witness and time, without retuning either. They show that the existence result is stable within this generator model. Preparing and measuring the large ensembles remains a separate physical problem.
