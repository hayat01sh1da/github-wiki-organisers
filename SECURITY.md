## Supported Versions

- We patch only the latest content on `master`, including automation under `.github/workflows`.
- Historical wiki exports or generated artifacts are snapshots and are not retroactively secured.

## Ecosystem & Compatibility

| Component / Workflow      | Version(s) / Tooling                 | Notes |
| ------------------------- | ----------------------------------- | ----- |
| OS baseline               | WSL (Ubuntu 24.04.3 LTS)            | Matches the environment documented in the README. |
| Ruby automation           | Ruby 4.0.1 (`.ruby-version`)        | Scripts rely on Bundler plus standard library; declare additional gems inside each tool. |
| Python automation         | CPython 3.14.3 (`.python-version`)  | Python helpers currently depend on the stdlib. Add `requirements.txt` if third-party packages are required. |
| GitHub Actions workflows  | Runs on GitHub-hosted Ubuntu images | Cron jobs send Slack notifications and mutate wiki content; keep action versions pinned. |

## Backward Compatibility

- CLI helpers and workflows are expected to remain compatible across Ruby 4.0.x and Python 3.14.x. When a workflow contract changes (e.g., new env vars), the corresponding README section and workflow dispatch docs will call it out.
- Archived wiki exports remain untouched; we do not backport automation fixes to historical snapshots.

## Reporting a Vulnerability

Please report issues privately via **GitHub Security Advisory** (preferred) — open through the repository’s **Security → Report a vulnerability** workflow.

Acknowledgement occurs and status updates follow as soon as possible.  
After remediation we publish guidance alongside required dependency updates.
