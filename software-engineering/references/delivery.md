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

## Completion report

After completing a task, report:

- what changed;
- what was validated;
- what was not validated and why;
- any remaining blocker or material uncertainty;
- a suggested commit message.

## Commit attribution

Suggested commit messages use `Assisted-By: <agent> <email>` instead of `Co-Authored-By:`.
