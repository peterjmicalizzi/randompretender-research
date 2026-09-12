# Licensing

This library is a public research record. Its contents are licensed so that anyone can read,
reuse, teach from, build on, and redistribute them, provided they say where the work came
from. The private application that runs [randompretender.com](https://randompretender.com/)
is a separate work and is **not** covered by anything in this file.

| Material | Licence | Full text |
|---|---|---|
| Code | Apache License 2.0 | [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt) |
| Everything else | Creative Commons Attribution 4.0 International (CC BY 4.0) | [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt) |

SPDX identifiers: `Apache-2.0` and `CC-BY-4.0`.

## Which licence applies to which file

**Code, under Apache 2.0:** source files (`.py`, `.lean`, `.sh`, `.js`, `.mjs`, `.ts` and
similar), everything under `tools/`, scripts inside `investigations/*/experiments/`, and
code blocks embedded in Markdown files, unless a file states otherwise at its top.

**Content, under CC BY 4.0:** prose in Markdown files, investigation briefs, claim and
execution records, result data and other JSON, issue and pull request templates, the
citation file, and images.

A file may carry its own header naming one of the two licences. The header wins over the
file-type rule. If you need a different arrangement for a particular contribution, say so
in the pull request before it is merged; it will be recorded in the file, not assumed.

## What is not relicensed by this policy

- **Third-party material.** Anything not created for this library keeps its own terms.
  Identify it in the file or in the pull request, with its source and licence. Do not add
  material whose licence you cannot grant. Papers are linked, never copied.
- **The licence texts and the Developer Certificate of Origin** are reproduced verbatim
  under their own terms and are not themselves relicensed.
- **The private application repository**, its source, builds, server configuration and
  data. Nothing in this library grants any right to it.
- **Names and trademarks.** CC BY 4.0 and Apache 2.0 both exclude trademark rights. "Random
  Pretender" and the site's identity are not licensed by this policy.

## Contributing under these terms

Contributions are accepted **inbound = outbound**: what you contribute is licensed to the
project and to everyone else under the same licence you received it under, Apache 2.0 for
code and CC BY 4.0 for content. There is no contributor licence agreement and no copyright
assignment. You keep your copyright.

Every commit must carry a **Developer Certificate of Origin** sign-off, the text of which
is in [`DCO.txt`](DCO.txt):

```
Signed-off-by: Your Name <your@email.example>
```

`git commit -s` adds the line for you. The sign-off is a personal statement that you wrote
the contribution or otherwise have the right to submit it under this policy. It records
that right; it does not transfer ownership, and it does not give the project permission to
change the licence on your contribution later. A sign-off is made by a person. An assisting
tool cannot make it on your behalf, and a `Co-Authored-By` trailer naming a model is
attribution, not a sign-off.

Employer-owned work needs the employer's permission before it is contributed. If you are
unsure whether you hold the rights, ask before opening the pull request rather than after.

## Citation and licence compliance

For scholarly citation, use the repository URL, the full commit SHA, and the record ID or
file path, as described in [`docs/EVIDENCE.md`](docs/EVIDENCE.md). Citation is not licence
compliance. Also comply with the applicable licence's notice, attribution and modification
requirements: Apache 2.0 requires that redistributed code keeps the licence and any
applicable notices and that modified files are marked as changed; CC BY 4.0 requires credit
to the source, a link to the licence, and an indication of any changes made.

The licences attach to the written presentation of the work. They do not, and cannot, make
a mathematical fact require attribution, which is why the contribution records, reviews
and citations in this library carry the credit chain rather than the licence alone.

## Effective date and earlier copies

This policy takes effect at the merge of the pull request that introduced it. Everything in
the repository at that commit was created for the library by its owner and is relicensed
under this policy by that merge. Copies or forks made before that commit were taken under
GitHub's terms of service only and carry no licence from this file.

## Reuse, including commercial reuse

Both licences allow commercial reuse, including by competitors. That is deliberate: a
course, a lab, or a company can adopt an investigation without asking for permission or
negotiating terms, and a licence once granted to a compliant recipient is not withdrawn.
The project competes on the application, the service around it, the community, and the
quality of the record, not on withholding the record.

This file is the project's stated policy, not legal advice. Before accepting substantial
employer-owned contributions or taking investment, have the ownership and contribution
arrangements reviewed by counsel.
