---
name: scientific-literature-evidence
description: Build and evaluate a research-literature corpus for a scientific landscape, attribution or priority question, version comparison, source conflict, or bounded absence search. Return source roles, claim-level evidence, version state, and search limits. Do not use for generic web search, bibliography formatting, or checking one already-supplied citation.
license: MIT. Adapted from texra-ai; see LICENSE.txt.
---

# Scientific Literature Evidence

Build the smallest source corpus that can answer the scientific question, then expose what that corpus does and does not establish.

## Define the evidence question

1. Identify whether the task is discovery, state-of-the-field synthesis, historical or priority attribution, version comparison, source-conflict resolution, or an absence claim.
2. Record the scientific scope, relevant time and version boundary, source types, and the evidence needed to stop. These modes do not share one universal preference for either breadth or recency.
3. Keep a single already-supplied citation-support judgment in `$scientific-claim-audit`; use this skill when constructing or comparing a source corpus is part of the work.

## Build and evaluate the corpus

- Use bibliographic records to establish identity and publication state, and the paper, supplement, data, or code containing the result to establish substantive support.
- Prefer controlling primary sources. Use reviews and secondary sources for routing, terminology, and synthesis, not as substitutes when the original evidence is available.
- For every consequential source, record its role, the exact proposition it supports, its scope, and a locator when available. Separate the source's statement from your inference.
- Read [source evaluation](references/source-evaluation.md) when versions differ, sources conflict, priority matters, or the result is a bounded negative search.

## Synthesize for scientific judgment

- Organize the result by the scientific distinction that changes interpretation, not by search order or an unstructured paper list.
- Expose disagreements through differences in definitions, assumptions, methods, samples, regimes, or versions before reconciling them.
- State remaining gaps and search boundaries. Repeated agreement can raise confidence but does not enlarge what the underlying evidence measures.
- Return an evidence corpus and synthesis. Compose `$scientific-claim-audit` when that evidence must determine the validity boundary of a manuscript claim, and `$structure-documentation` when durable literature-review prose is requested.
