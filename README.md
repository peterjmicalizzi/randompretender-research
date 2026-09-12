# Random Pretender Research Library

**The site is the laboratory. This repository is the shared lab notebook. Bring whichever AI or computation tool you use; leave a contribution someone else can follow.**

Explore at [randompretender.com](https://randompretender.com/). Start with [Single-qubit gates and the 600-cell](investigations/gates-600-cell/BRIEF.md).

## Participate in a minute

- [Ask a question, share an observation, or propose a feature](https://github.com/peterjmicalizzi/randompretender-research/issues/new?template=contribution.yml). One sentence is enough to start. Add a site link or exported study packet if you have one.
- [Challenge a result or report a counterexample](https://github.com/peterjmicalizzi/randompretender-research/issues/new?template=challenge.yml).
- [Record a reproduction or scoped review](https://github.com/peterjmicalizzi/randompretender-research/issues/new?template=review.yml).
- [Browse open work](https://github.com/peterjmicalizzi/randompretender-research/issues) or [join the discussion](https://github.com/peterjmicalizzi/randompretender-research/discussions).
- For files, **fork this repository**, edit your fork, and open a pull request. [Contribution guide](CONTRIBUTING.md).

Anyone can read without an account. GitHub requires an account to comment, open an issue, or submit a pull request. Only the repository owner and explicitly authorized maintainers can merge. Community reactions indicate interest, not mathematical validity.

## Take the context to your AI

Open [the gate investigation brief](investigations/gates-600-cell/BRIEF.md), press **Y** on GitHub to pin the file to a commit, then download its raw contents. It includes the question, conventions, open tasks, references, and the return format. For a calculation, take the referenced script and result files too. No original chat is required.

Ask: “Explain this investigation, identify what the evidence establishes, and help me contribute to one open question. Keep the starting revision and assumptions in the response.”

## What is available now

This public library supports issues, comments, discussions, forks, reviewed pull requests, a self-contained investigation brief, and a small exact-arithmetic starter experiment. The starter has one implementation and internal checks; it has **no independent reproduction or specialist endorsement yet**.

Automatic capture from the website, automated evidence assessments, equivalence-aware object identity, and automatic dependency notifications are next-stage work. A site URL preserves a view's parameters, **not an archived software environment**. This repository does not currently archive or recreate historical application builds.

## How this library is organized

| Location | Purpose |
|---|---|
| `investigations/` | Questions, briefs, mathematical conventions, and workspace manifests |
| `investigations/.../claims/` | Precisely scoped statements with evidence references |
| `investigations/.../experiments/` | Inspectable source and recorded outputs |
| `templates/` | Optional structure for substantial contributions and reviews |
| `docs/` | Governance, evidence rules, and the site-integration roadmap |
| `tools/` | A local, data-only library validator |

GitHub issue/PR URLs identify contributions. A repository-relative record ID identifies a claim or experiment; cite it with a **full commit SHA** to identify the exact revision. File paths and `main` URLs alone are not immutable citations.

## Production boundary

This is a new repository with a fresh history, separate from the private application repository. It contains no production source, server credentials, deployment hooks, or access to the live server. GitHub Actions are disabled. Submitted scripts and Lean files do not run automatically. Opening or merging an issue/PR does not deploy anything or certify a result.

## Licence

Code is under the [Apache License 2.0](LICENSES/Apache-2.0.txt); briefs, records, data and other content are under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Contributions are accepted on the same terms with a [Developer Certificate of Origin](DCO.txt) sign-off. Details, file-type rules and exceptions are in [LICENSING.md](LICENSING.md). The private application is licensed separately.

[Permissions and governance](docs/GOVERNANCE.md) · [Evidence and attribution](docs/EVIDENCE.md) · [Security](SECURITY.md) · [Licensing](LICENSING.md) · [Next integration steps](docs/ROADMAP.md)
