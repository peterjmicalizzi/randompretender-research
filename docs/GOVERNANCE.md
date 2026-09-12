# Permissions and workflow

| Participant | Can do | Cannot do by default |
|---|---|---|
| Public reader | Read and download public content | Change the shared record |
| Signed-in GitHub participant | Comment, open issues/discussions, fork, propose PRs | Merge into upstream, access private application/server |
| Scoped reviewer | Attach an assessment to an exact revision | Confer authority outside the scope reviewed |
| Repository owner | Triage, moderate, review, merge PRs, administer repository | Treat popularity or merge admission as mathematical proof |

Initially Peter's GitHub account is the sole maintainer. AI agents using that account are not independent approvers. Main requires a PR, resolved review conversations, and forbids force pushes/deletions. There is initially no mandatory second approval because there is no second independent maintainer; adding one is a separate owner decision. There are no required CI checks because Actions are disabled. Local validation and diff review are documented responsibilities, not an enforced automated certification.

Comments and exploratory contributions can be published without formal verification. Substantial findings are summarized into versioned records through PRs. Labels classify topics and contribution types; they do not assign mathematical truth. A closed issue can mean a discussion was concluded, duplicated, or superseded—not that its statement was proved.

## Processing a contribution

1. Participant submits a sentence, optional site link/packet, or fork PR.
2. Maintainer identifies the investigation and requests missing context only when needed.
3. Evidence and scoped reviews are attached, with authors and exact revisions.
4. Maintainer checks provenance, rights to publish, sensitive content, and record links.
5. Merge adds a contribution to the public record. Site development remains a separate process in the private application repository.

Use GitHub reactions to indicate interest or clarity. Use a reproduction record for a claim of reproducibility. Record disagreements and avoid presenting a majority vote as mathematical evidence. No participant may purchase a favorable assessment.

## Ownership and continuity

Only grant write/admin permissions deliberately to named maintainers. Researchers do not need write access to contribute. Do not share the owner's GitHub credentials with participants. Contributions remain accessible in forks; revoking access cannot recall material already published publicly.

Governance changes use PRs too. Keep the distinction between scientific review and repository administration visible.
