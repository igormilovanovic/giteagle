# CLAUDE.md - Project Rules

## Project

- **Repo**: `igormilovanovic/giteagle`
- **Default branch**: `master`
- **Language**: Python (3.9+)
- **Package manager**: `uv`

## GitHub Workflow Rules

All work MUST follow the GitHub issue/PR workflow. Never push directly to `master`.

### 1. Issues First

- Before starting any non-trivial work, create a GitHub issue using `gh issue create`.
- Assign yourself to the issue.
- Use descriptive titles and label issues appropriately (`bug`, `enhancement`, `docs`, etc.).
- Reference related issues when applicable.

### 2. Branch Naming

- Always create a feature branch from `master` before making changes.
- Use the convention: `<type>/<short-description>` (e.g., `fix/typo-in-readme`, `feat/add-auth`, `chore/update-deps`).
- Branch names should reference the issue number when applicable: `fix/123-broken-parser`.

### 3. Pull Requests

- Push your branch and create a PR using `gh pr create`.
- Link the PR to its issue using `Closes #<issue-number>` in the PR body.
- PRs must target `master`.
- PR titles should be concise (<70 chars) and descriptive.
- PR body must include a `## Summary` and `## Test plan` section.
- Request reviews when appropriate using `gh pr edit --add-reviewer`.

### 4. Verify Code via GH Actions

After every push, you MUST verify the code is correct by monitoring CI:

- Run `gh pr checks --watch` to wait for all checks to complete.
- If any check fails, run `gh run view --log-failed` to inspect the failure logs.
- Diagnose and fix the failure locally, then push again.
- Repeat until all checks pass — do not merge with failing checks.
- Do NOT rely solely on local test runs. GH Actions is the source of truth for correctness (it tests across Python 3.9-3.12).

**Verification loop after pushing:**

```bash
gh pr checks --watch          # Wait for CI to finish
gh run list -b <branch> -L 1  # Find the latest run
gh run view <run-id> --log-failed  # Inspect failures if any
```

- All PRs must pass the full CI workflow (lint, type-check, tests on Python 3.9-3.12) before merging.
- Never bypass or skip checks. Never use `--no-verify`.

### 5. Merging

- Prefer squash merges for clean history.
- Delete the branch after merging using `gh pr merge --squash --delete-branch`.
- Never force-push to `master`.

### 6. Issue Management

- Close issues via PR merges (using `Closes #N`), not manually.
- Use `gh issue list` to review open issues before starting new work.
- Use `gh issue comment` to provide status updates on long-running work.

## Development Commands

```bash
uv sync --all-extras          # Install dependencies
uv run ruff check src tests   # Lint
uv run ruff format src tests  # Format
uv run mypy src --ignore-missing-imports  # Type check
uv run pytest --cov           # Test with coverage
```

## Code Style

- Follow existing patterns in the codebase.
- All code must pass `ruff check` and `ruff format --check`.
- All code must pass `mypy` type checking.

## Attribution

- NEVER add AI-generated signatures, badges, or footers to commits, PRs, issues, or code. This includes lines like "Generated with Claude Code", "Co-Authored-By: Claude", or any similar attribution. All contributions should appear as normal developer contributions.
