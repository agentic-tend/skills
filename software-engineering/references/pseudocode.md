# Software structured IR

Use pseudocode as a task-local structured intermediate representation when software logic or data evolution must become reviewable while replaceable target-language mechanics remain open.

## Select the interaction path

Apply the L0 turn-continuation contract to software:

- When pseudocode is the requested artifact, resolve any user-owned meaning exposed by the projection, then deliver the smallest complete projection and stop.
- When the user requests discussion, clarification, or pre-implementation review, expose the projection with the earliest user-owned open relation and wait for the response; when no such relation is open, invite review and wait.
- When implementation is directly requested and the next responsibility boundary, mutable-state owner, concurrency boundary, lifecycle, multi-step data or control flow, or failure-recovery path needs a reviewable structure, expose the projection and continue within established authority.
- When the projection exposes user-owned meaning, route that relation through the applicable clarification boundary.

A supplied equivalent IR becomes the live sketch and is updated in place. Mechanical edits, structurally inferable local realization, factual explanation, and status reporting continue through their ordinary task path.

## Represent the next boundary

Project the smallest responsibility boundary current review or implementation needs. Establish its responsible actor or state owner, accepted input, observable output or effect, failure behavior, and dependency on adjacent boundaries. When meaning remains open, identify its decision owner. Within that boundary, include the ordered transformations, branches, data or state ownership, state transitions, external effects, and failure propagation that distinguish the intended realization.

At one responsibility layer, this projection is the `how` that realizes its parent boundary and the `what` that its child realization must preserve. Use domain terms and identifiers inside stable relations. Include a decision owner, state owner or actor, relation or condition, affected object or state, and observable transition or result when each role changes judgment. Target-language syntax, private helper layout, and replaceable mechanics remain with realization.

A small IR may fit on one line. Expand recursively when a lower responsibility boundary becomes independently meaningful.

## Route authority and feedback

Link each projected relation to the established acceptance criterion that constrains it. Evidence updates the affected relation or returns a changed user-owned contract or oracle to its decision owner.
