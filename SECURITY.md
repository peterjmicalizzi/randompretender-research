# Security and reporting

This repository is a public discussion and research-artifact boundary. It has no credentials, production connection, self-hosted runners, or automatic code execution. GitHub Actions are disabled at repository level. The application remains in a separate private repository.

Do not put vulnerabilities containing secrets or exploit details in public issues. Use GitHub's **Security → Report a vulnerability** private reporting feature. If unavailable, contact the repository owner privately through their GitHub profile before sending sensitive material. Public comments are not a confidential channel.

Do not load-test the live application or send experiment batches to its API as part of contributing here. Use local experiments or an explicitly authorized isolated test environment.

## Maintainer execution boundary

- Inspect all contributed text, links, source, workflow files, dependency manifests, and binaries before acting on them.
- Never run PR code, install its dependencies, open an active notebook, or compile its Lean files in an environment holding credentials or private data. Proof checking is not a sandbox.
- No `pull_request_target`, comment-command bot, Actions workflow, webhook, deployment key, or website ingestion is provisioned here.
- Keep main protected, force pushes/deletions blocked, and changes routed through PRs. Review the latest revision before merging. GitHub credentials held by an owner remain privileged; branch rules are not a substitute for careful agent authorization.
- A future website reader must treat library content as data, escape/sanitize displayed text, avoid arbitrary URL fetching, and never execute a submitted operation outside a validated and resource-limited interface.

This boundary reduces production exposure; it is not a guarantee that public content, external links, or code are harmless.
