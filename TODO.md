# TODO

## High Priority

- [ ] `giteagle standup` — daily activity report across repos (#18)
- [ ] `giteagle prs` — cross-repo open PR dashboard with review/CI status (#19)
- [ ] `giteagle stats` — DORA-style PR metrics (TTM, TTFR, merge rate, throughput) (#20)
- [ ] Add CLI tests (currently 0% coverage on all commands)
- [ ] Export to CSV/JSON (`--format json|csv` on CLI commands)
- [ ] Expose activity filters on CLI (`--type commit`, `--author alice`, etc.)

## Medium Priority

- [ ] GitLab integration (base `PlatformClient` interface already exists)
- [ ] Bitbucket integration (same pattern as GitLab)
- [ ] Fix silent error suppression in timeline command (`except Exception: pass`)

## Low Priority / Future

- [ ] Slack/Discord notifications
- [ ] Web dashboard
- [ ] Team/group analytics
