# Contributing

## A question or observation

Use an issue. Add one sentence describing what you noticed or want to study. A site URL, packet, or screenshot is optional at submission; reviewers may need more context before assessing the claim. Never attach passwords, tokens, personal student data, private conversations, or files you cannot share publicly.

Comments and Discussions are for exploration. Use an issue when there is a concrete question or task to track. Feature proposals belong here too; library acceptance is not approval to modify or deploy the application.

## A challenge

Link the statement you challenge and explain why. Include the exact revision and conditions when available. An unresolved challenge is a contribution, not an accusation. The original record stays visible; a checked counterexample can refute the original claim while a narrower revision remains open.

## A file contribution

1. Fork the public library; create a branch for one contribution.
2. Record the starting upstream commit. Use the current investigation's conventions or explicitly state changes.
3. Add the smallest useful explanation and evidence. Use `templates/contribution.md` if helpful; there is no requirement to fill a large form to start.
4. For a new claim or run use a new ID; preserve older evidence. Corrections link to the original rather than silently replacing its meaning.
5. Open a pull request explaining what is new, what was checked, and any unresolved question. Credit authors, tools, prior work, and scoped reviewers. Do not claim that an AI is an independent mathematical reviewer.
6. The maintainer reviews the actual diff and decides whether to merge. Admission to the library means the contribution was accepted into the record, not that every mathematical claim was endorsed.

Prefer readable Markdown, JSON, Python, or Lean source. Keep individual files below 2 MB for this initial library. Link large artifacts to immutable releases with hashes and retention details; do not use executable archives, symlinks, submodules, or committed runtime environments. Reference papers by stable links rather than copying their PDFs or text without permission.

The local validator checks record consistency and the starter's artifact hashes; it does not execute submitted code or verify arbitrary mathematics:

```sh
python tools/validate_library.py
```

Maintainers must review changes to the validator before running it. Run unfamiliar experiments only after inspection in an isolated, disposable environment with no credentials, private mounts, or production access. There is no automatic public submission runner.

## Attribution and notifications

Issue, comment, and PR authorship is preserved by GitHub. Cite a scoped review using its comment/PR URL and the full revision reviewed. Watch or subscribe to an investigation issue to receive GitHub notifications; this library does not yet automatically notify every mathematical dependency.

## Licensing

Read `LICENSING.md` before contributing. Do not submit third-party material under a license you cannot grant. Any future dual-license policy must be explicit; it cannot silently relicense earlier contributions.
