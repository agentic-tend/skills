# Software feedback loop

This reference defines how to turn sparse terminal acceptance into useful intermediate evidence without inventing requirements or optimizing against an invalid proxy.

## Start from the objective

State the observable goal, current evidence, stopping condition, and remaining uncertainty. Separate user-owned semantics from implementation questions: ask the user only when the unresolved choice changes purpose, behavior, scope, authority, or acceptance.

Form the smallest falsifiable hypothesis that would explain the uncertainty. Do not start from a preferred fix, abstraction, optimization, or defensive check.

## Choose a discriminating surface

Use the cheapest feedback surface that can distinguish the live alternatives. Depending on the task, that may be source or dependency inspection, a compiler or type checker, a focused test, an error and stack trace, logs, runtime introspection, a profiler, an external oracle, or user review. Add temporary instrumentation when the system cannot expose the needed distinction.

Define what each possible result would mean before running the probe. Preserve relevant inputs, versions, environment, commands, and raw output so later interpretation does not depend on memory or a preferred narrative.

## Interpret before changing

Classify the observation before editing:

- implementation evidence falsifies or supports the working hypothesis;
- the test, benchmark, grader, or proxy does not represent the real goal;
- environment or dependency state invalidates the comparison;
- new semantic ambiguity requires human judgment;
- the evidence is insufficient and needs a different probe.

A tool result is an observation, not automatically a requirement. A possible edge case, clearer error, stricter type boundary, overflow check, retry, or fallback becomes durable behavior only when it follows from the contract or demonstrated pressure. Error quality matters, but improving it does not authorize broadening the accepted input set, changing dispatch, catching away root-cause context, or guaranteeing failures the API never promised.

Update the hypothesis or measurement edge that the observation actually challenges, then run the next cheapest discriminating step. Do not rerun stochastic work until it passes, layer safeguards onto an unverified premise, or treat more conservative code as inherently more correct.

## Close and learn

Stop when the agreed evidence satisfies the goal. Report bounded claims: what was observed under which conditions, what remains unverified, and which conclusion depends on human acceptance.

Promote a lesson into a contract, test, skill, or rule only when its owner is clear and repeated evidence shows future decisions would otherwise regress. Confirmed failures may become regression cases; transient hypotheses, probe output, and one-off environment facts remain in the execution record.
