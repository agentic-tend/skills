# Julia feedback surfaces

Use this reference to select evidence for the current uncertainty. It routes to Julia-owned feedback surfaces; it does not make their outputs self-interpreting or turn current platform facts into permanent rules.

## Establish the observation context

Record `VERSION`, the project's Julia compatibility, and the smallest reproducer. When relevant, also record `Sys.WORD_SIZE`, `Sys.KERNEL`, `Sys.ARCH`, package versions, environment variables, Julia thread pools, and active linear-algebra configuration through [`BLAS.get_config()`](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/).

Open documentation for the project's Julia release, not an unverified development page. When an API or note is absent from that version's page, use installed-version help, source, or a minimal executable probe before relying on it.

## Route by uncertainty

For applicability and dispatch, inspect [`methods`](https://docs.julialang.org/en/v1/base/base/#Base.methods), [`@which` and `@code_lowered`](https://docs.julialang.org/en/v1/stdlib/InteractiveUtils/), the actual method table, and focused calls at the accepted and rejected boundary. Use the [Types](https://docs.julialang.org/en/v1/manual/types/), [Methods](https://docs.julialang.org/en/v1/manual/methods/), and [Conversion and Promotion](https://docs.julialang.org/en/v1/manual/conversion-and-promotion/) chapters to interpret the result. Let the contract choose the widest valid type set; do not infer a signature from performance folklore.

For correctness and error behavior, begin with the smallest focused [`Test`](https://docs.julialang.org/en/v1/stdlib/Test/) oracle that represents the contract. Preserve the exception and its [`catch_backtrace`](https://docs.julialang.org/en/v1/manual/stacktraces/) when diagnosing a deep failure; inspect `current_exceptions()` when error handling creates a secondary exception. Improve error quality only at a justified public boundary, without catching away the root cause or promising new failure modes by default.

For inference and generated-code questions, use [`@code_warntype`](https://docs.julialang.org/en/v1/stdlib/InteractiveUtils/) as a hypothesis surface, then connect highlighted types to measured behavior. Non-concrete output is not automatically a performance defect. Escalate to `@code_typed`, LLVM, or native code only when the higher-level evidence cannot distinguish the cause.

For latency or allocation, separate cold compilation from warmed execution with `@timed`; use `@allocated` for a focused steady-state allocation count and [`Profile`](https://docs.julialang.org/en/v1/manual/profile/) or `Profile.Allocs` to locate workload cost. Preserve the same inputs and correctness oracle before and after. Use external benchmark packages only when the project already allows them or the user approves the dependency.

For threading and BLAS, first record Julia thread pools, CPU allocation or affinity when available, environment configuration, and `BLAS.get_config()`. Treat `BLAS.set_num_threads` as a backend request, not proof of the effective hardware behavior; consult the project's Julia [LinearAlgebra](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/) and [Performance Tips](https://docs.julialang.org/en/v1/manual/performance-tips/) pages plus the active backend's documentation. Compare warmed configurations on the actual workload and check correctness rather than assuming more threads are faster.

For suspicious migration code or familiar-looking syntax, run a tiny semantic example with representative complex values, shapes, indices, mutation, or state lifetime, then consult [Noteworthy Differences](https://docs.julialang.org/en/v1/manual/noteworthy-differences/) and the specific Julia chapter it links to. Reconstruct Julia semantics instead of transliterating Python or MATLAB surface syntax.

## Interpret and close

Before running a probe, state what each outcome would distinguish. Afterwards classify whether the implementation hypothesis, oracle, environment, backend assumption, or contract needs revision. A request accepted by an API, a green test, or a faster sample supports only a bounded observation under the recorded conditions.

Stop when the project's acceptance evidence is complete. Keep platform snapshots and raw probe output in the task, issue, or pull-request record. Persist a Julia conclusion only through the skill's admission gate; do not turn a one-machine result into static language guidance.
