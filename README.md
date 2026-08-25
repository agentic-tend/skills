# Skills

This repository owns Agentic Tend's reusable skills layer, dogfooded in Codex before publication.

Each top-level skill directory is independently discoverable through its `SKILL.md` entrypoint. The collection follows the open [Agent Skills](https://agentskills.io/home) format: compatible agents discover concise metadata first and load full instructions and bundled resources only when task traits match. Agentic Tend's [capability model](https://github.com/agentic-tend/.github/blob/main/docs/capability-model.md) owns the primitive ontology, its [context ownership model](https://github.com/agentic-tend/.github/blob/main/docs/context-ownership.md) owns placement and activation boundaries, and this README instantiates the current capability graph. Semantic ownership, activation, and mechanical enforcement remain distinct.

Skills are composable capabilities dispatched from task traits, not mutually exclusive task owners. Modularity encapsulates reusable logic and authority routing; composability exposes ports through which selected capabilities consume the same task data and contribute decisions or evidence.

## Capability topology

Each row describes ports, not an exclusive category.

| Capability | Consumes | Provides | Composition seam | Boundary |
| --- | --- | --- | --- | --- |
| [`bootstrap-project-context`](bootstrap-project-context/SKILL.md) | Repository state and persistence pressure | Context ownership migration | Composes with the affected concern and prose capabilities | Does not own ordinary implementation |
| [`clarifying-contracts`](clarifying-contracts/SKILL.md) | An unresolved user-owned semantic choice | An approved contract | Adds authority resolution to any mixed task | Does not resolve discoverable facts |
| [`multi-agent-evidence`](multi-agent-evidence/SKILL.md) | Task data with independently formable, held-out, or falsifiable evidence | A human-visible plan, dynamic evidence ports, recursive feedback, and provenance-aware delivery | Places selected capability work in separate contexts without changing its semantic owner | Does not activate for latency alone or prescribe agent micro-orchestration |
| [`scientific-literature-evidence`](scientific-literature-evidence/SKILL.md) | A literature question requiring a source corpus, attribution, version comparison, conflict resolution, or bounded absence search | Source roles, claim-level evidence, synthesis, version state, and search boundaries | Supplies literature evidence to scientific claim audit and durable research prose | Does not own manuscript-claim validity, generic web search, or bibliography formatting |
| [`scientific-claim-audit`](scientific-claim-audit/SKILL.md) | A specific scientific claim or objection and its controlling evidence | Claim-level support status, scope, findings, and unresolved gaps | Consumes formal, computational, or literature evidence and supplies scientific meaning to prose or delivery capabilities | Does not activate merely because content is scientific or own final prose and artifact syntax |
| [`referee-response`](referee-response/SKILL.md) | An exact scientific referee comment, current manuscript state, and established evidence | A scoped response and manuscript-revision map | Supplies established meaning to prose organization and repository-specified artifact workflows | Does not establish contested scientific validity or authorize manuscript and submission actions |
| [`software-engineering`](software-engineering/SKILL.md) | Software contract and implementation evidence | Behavior, topology, testing, and delivery decisions | Composes with language and prose capabilities | Does not own host-language syntax |
| [`julia-development`](julia-development/SKILL.md) | Julia project, version, source, and renderer evidence | Julia-specific decisions and host conventions | Composes with software, structure, and Markdown capabilities | Does not own language-independent software topology |
| [`structure-documentation`](structure-documentation/SKILL.md) | Established durable meaning and the reader's task | A language-independent reading path | Composes with artifact-language and host capabilities | Does not decide meaning or syntax |
| [`markdown-authoring`](markdown-authoring/SKILL.md) | A Markdown artifact and renderer facts | Markdown syntax and generic or GitHub rendering realization | Composes with structure and host extensions | Does not own prose semantics or host-specific extensions |
| [`obsidian-cli`](obsidian-cli/SKILL.md) | Obsidian index or runtime state | Runtime-aware Obsidian operations | Composes with Markdown and structure only when content changes | Does not own ordinary filesystem editing |

## Validate

Validate every published skill against the Agent Skills specification:

```bash
python3 -m unittest discover -s tests
gh skill publish --dry-run
```

## Provenance

[`clarifying-contracts`](clarifying-contracts/SKILL.md) adapts Superpowers' brainstorming workflow and Matt Pocock's grilling[^grilling]. [`obsidian-cli`](obsidian-cli/SKILL.md) adapts and narrows Kepano's upstream [Obsidian CLI skill](https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-cli).

The scientific capabilities adapt distinct parts of TeXRA's MIT-licensed workflows:

- [`scientific-claim-audit`](scientific-claim-audit/SKILL.md) retains validity discipline from [`manuscript-review`](https://github.com/texra-ai/texra-scientific-skills/tree/main/skills/manuscript-review) and [`inline-paper-critic`](https://github.com/texra-ai/texra-scientific-skills/tree/main/skills/inline-paper-critic).
- [`scientific-literature-evidence`](scientific-literature-evidence/SKILL.md) refactors [`literature-search`](https://github.com/texra-ai/texra-scientific-skills/tree/main/skills/literature-search) around source roles, versions, and bounded scientific synthesis.
- [`referee-response`](referee-response/SKILL.md) adapts response-delivery constraints from `manuscript-review` and [`writing-commenter`](https://github.com/texra-ai/texra-scientific-skills/tree/main/skills/writing-commenter), while leaving prose organization to `structure-documentation` and artifact realization to repository instructions and current tools.

The physics-journal specialization of `referee-response` follows current APS and IOP author guidance; general online writing skills remain design references rather than procedural authorities.

## See also

- The [Agentic Tend principles](https://github.com/agentic-tend/.github/blob/main/docs/principles.md) own pressure-driven behavior and its specialization to persistent structure.
- The [presentation model](https://github.com/agentic-tend/.github/blob/main/docs/presentation.md) owns progressive disclosure for human review.
- The [multi-agent evidence model](https://github.com/agentic-tend/.github/blob/main/docs/multi-agent.md) owns the effective theory for observable agent ports, feedback topology, and evidence separation.
- The [capability-composition examples](https://github.com/agentic-tend/.github/blob/main/docs/capability-composition.md) illustrate composition without prescribing a fixed workflow.
- The [organization roadmap](https://github.com/agentic-tend/.github/blob/main/docs/roadmap.md) tracks evidence and extension work spanning multiple tooling layers.

## License

The repository is available under the [MIT License](LICENSE). Each independently installable skill bundles its complete terms and any required upstream notices.


[^grilling]: Matt Pocock, [*grilling*](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): one-question-at-a-time clarification of plans and decisions.
