# Computational evidence

Read this reference before endorsing or challenging a numerical result, benchmark, convergence statement, extrapolation, or figure backed by data or code.

## Establish provenance and scope

- Identify the model or data-generating process, system or sample, geometry and boundary conditions when applicable, parameters, observable or metric, initialization or sector, estimator, uncertainty treatment, and implementation version that produced the claim.
- Trace the narrow dependency chain across prose, equations, captions, plotted values, raw data, and generating code. Resolve disagreement at the artifact that actually generates or measures the result.
- Record which convergence controls, finite-size checks, baselines, ablations, or repeated runs were performed. Do not infer an omitted check from a successful optimizer, build, or visually plausible plot.

## Bound the conclusion

- Benchmark agreement validates only the quantities, regimes, tolerances, and baselines actually compared. Efficiency, scalability, novelty, and broader physical or scientific conclusions require their own evidence.
- Keep finite-system, finite-sample, discretization, truncation, variational, and initialization limits attached to the claim. Extrapolation requires evidence for the extrapolation, not only a well-converged point.
- Distinguish a diagnostic from the scientific state or mechanism it is used to infer. When multiple explanations remain compatible with the measured observable, return that ambiguity.
- If only explicitly constructed alternatives were compared, state the result relative to those alternatives rather than as a global optimum or exhaustive exclusion.

## Calibrate the finding

Distinguish a verified mismatch, a likely issue with incomplete provenance, an untested extrapolation, a missing report of validation, and material independently reproduced or found consistent. State exactly what was rerun, recomputed, inspected, or compared and what remains outside the check.
