# TODO

## High Priority

- [ ] Add CLI tests (currently 0% coverage on all 5 commands)
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
