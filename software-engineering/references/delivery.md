# Software delivery

This reference defines when local software work is technically complete and how to hand it back without inferring authority for external actions.

## Definition of done

A task is technically complete only when:

- the diff is limited to the approved scope;
- relevant tests were added or updated when behavior changed;
- relevant validation commands ran, or the reason for not running them is stated.

Repository-specific validation commands belong in that repository's `AGENTS.md` once its language and tooling make them durable local facts.

Do not report a validation command as completed without command or output evidence. When execution is unavailable, state that the check was not run.

## Repository actions

Technical completion does not authorize a commit, push, pull request, publication, release, or archive. Follow the active authority boundary and leave external delivery to the user unless that action was explicitly requested.

## Software handoff

Specialize the active interaction contract from current software task data. Layer the handoff by reader responsibility: lead with the achieved outcome and affected public interface; then give material contract changes, validation, blockers, and uncertainty; keep implementation mechanics and raw evidence in the deepest reachable layer. A reader responsible only for the public interface should be able to stop after the first layer.

Promote any detail that changes judgment into the earliest sufficient layer. A one-line public-contract change, failed or incomplete validation, blocker, or material uncertainty takes precedence over extensive inferable implementation detail. Keep commands, raw output, and the underlying diff reachable when they exist.

State what validation ran, what did not run and why, and any remaining blocker or material uncertainty. Include a suggested commit message only when the user requests a commit, pull-request package, or commit-level delivery prose.

## Commit attribution

When a suggested commit message is in scope, use `Assisted-By: <agent> <email>` instead of `Co-Authored-By:`.
