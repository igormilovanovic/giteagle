# Giteagle

**Get a bird's eye view of your repositories.**

[![Tests](https://github.com/pletisan/giteagle/actions/workflows/test.yml/badge.svg)](https://github.com/pletisan/giteagle/actions/workflows/test.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Giteagle helps engineering teams track activities across multiple repositories. When your project spans dozens of repos with contributions from multiple teams, staying on top of what's happening becomes challenging. Giteagle aggregates commits, pull requests, and issues into a unified view.

## Why Giteagle?

Modern software development often involves **multi-repository architectures**:

| Scenario | Example Projects | Challenge |
|----------|------------------|-----------|
| **Microservices** | Uber, Netflix, Spotify | 100s of service repos, hard to track cross-service changes |
| **Platform ecosystems** | Kubernetes (70+ repos), HashiCorp (Terraform providers) | Core + plugins/providers across many repos |
| **Monorepo alternatives** | Google's approach before Piper | Related projects in separate repos need coordination |
| **Open source foundations** | Apache, CNCF, Linux Foundation | Governance across project portfolios |

### Real-World Examples

**Kubernetes Ecosystem** - The Kubernetes project spans 70+ repositories:
- `kubernetes/kubernetes` - Core
- `kubernetes/dashboard` - Web UI
- `kubernetes/ingress-nginx` - Ingress controller
- `kubernetes/client-go` - Go client library
- ...and many more

**HashiCorp Terraform** - Terraform's provider ecosystem:
- `hashicorp/terraform` - Core
- `hashicorp/terraform-provider-aws` - AWS provider
- `hashicorp/terraform-provider-google` - GCP provider
- Hundreds of community providers

**Your Company** - Typical enterprise setup:
- `company/api-gateway`
- `company/user-service`
- `company/billing-service`
- `company/shared-libs`
- `company/infrastructure`

## Features

- **Unified Activity Feed** - See commits, PRs, and issues across all your repos in one view
- **Contributor Insights** - Track who's contributing where and how much
- **Timeline Analysis** - Visualize activity patterns over time
- **Cross-Repo Aggregation** - Combine statistics from multiple repositories
- **Beautiful CLI Output** - Rich terminal formatting with tables and charts
- **GitHub Integration** - Full support for GitHub API with rate limiting and pagination

## Quick Start

### Installation

```bash
# Using uv (recommended)
uv tool install giteagle

# Or with pip
pip install giteagle

# Or install from source
git clone https://github.com/pletisan/giteagle.git
cd giteagle
uv sync
```

### Configuration

Set your GitHub token for API access:

```bash
# Via environment variable (recommended)
export GITHUB_TOKEN=ghp_your_token_here

# Or create a config file
mkdir -p ~/.config/giteagle
cat > ~/.config/giteagle/config.yaml << EOF
github:
  token: ghp_your_token_here
default_platform: github
EOF
```

### Basic Usage

```bash
# List repositories for a user or organization
giteagle repos kubernetes --org

# View recent activity for a repository
giteagle activity kubernetes/kubernetes --days 7

# Get aggregated summary across multiple repos
giteagle summary kubernetes/kubernetes kubernetes/dashboard kubernetes/ingress-nginx

# View activity timeline
giteagle timeline hashicorp/terraform hashicorp/terraform-provider-aws --days 30
```

## Usage Examples

### Example 1: Track a Microservices Project

You're leading a team with 5 microservices. Get a weekly summary:

```bash
# See what happened across all services this week
giteagle summary \
  mycompany/api-gateway \
  mycompany/user-service \
  mycompany/order-service \
  mycompany/payment-service \
  mycompany/notification-service \
  --days 7
```

Output:
```
╭─────────────────────────────────────╮
│        Summary (last 7 days)        │
├─────────────────────────────────────┤
│ Total Activities: 47                │
│ Repositories: 5                     │
│ Contributors: 8                     │
╰─────────────────────────────────────╯

By Activity Type
┌──────────────┬───────┐
│ Type         │ Count │
├──────────────┼───────┤
│ commit       │    32 │
│ pull_request │    12 │
│ issue        │     3 │
└──────────────┴───────┘

Top Contributors
┌──────────────┬────────────┐
│ Username     │ Activities │
├──────────────┼────────────┤
│ alice        │         15 │
│ bob          │         12 │
│ charlie      │          9 │
└──────────────┴────────────┘
```

### Example 2: Monitor Open Source Dependencies

Track activity in critical dependencies your project relies on:

```bash
# Monitor key libraries you depend on
giteagle summary \
  pallets/flask \
  psf/requests \
  encode/httpx \
  --days 14
```

### Example 3: Activity Timeline for Sprint Planning

Visualize development patterns to plan capacity:

```bash
giteagle timeline myorg/backend myorg/frontend --days 30 --granularity week
```

Output:
```
╭──────────────────────────────────────╮
│     Activity Timeline (weekly)       │
╰──────────────────────────────────────╯
2024-01-01: ████████████████████ 45
2024-01-08: ██████████████████████████ 58
2024-01-15: ████████████ 27
2024-01-22: ██████████████████████████████ 67
2024-01-29: ████████████████ 35
```

### Example 4: View Detailed Repository Activity

Drill into a specific repository:

```bash
giteagle activity facebook/react --days 3 --limit 20
```

Output:
```
╭────────────────────────────────────────────────────╮
│                 facebook/react                      │
│  A declarative, efficient, and flexible JavaScript │
│  library for building user interfaces.              │
╰────────────────────────────────────────────────────╯

Activity (last 3 days)
┌──────────────┬────────────────────────────────────┬───────────┬──────────────────┐
│ Type         │ Title                              │ Author    │ Date             │
├──────────────┼────────────────────────────────────┼───────────┼──────────────────┤
│ commit       │ Fix hydration mismatch warning     │ gaearon   │ 2024-01-15 14:32 │
│ pull_request │ Add new concurrent features        │ acdlite   │ 2024-01-15 11:20 │
│ commit       │ Update scheduler priority levels   │ sebmarkba │ 2024-01-14 16:45 │
└──────────────┴────────────────────────────────────┴───────────┴──────────────────┘
```

## CLI Reference

### Commands

| Command | Description |
|---------|-------------|
| `giteagle repos <owner>` | List repositories for a user or organization |
| `giteagle activity <repo>` | Show recent activity for a repository |
| `giteagle summary <repos...>` | Aggregated summary across multiple repos |
| `giteagle timeline <repos...>` | Activity timeline visualization |
| `giteagle config` | Show current configuration |

### Common Options

| Option | Description |
|--------|-------------|
| `--days N` | Number of days to look back (default: 7) |
| `--limit N` | Maximum number of items to show (default: 50) |
| `--org` | Treat owner as organization (for `repos` command) |
| `--granularity` | Timeline granularity: day, week, month |

## Development

### Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
# Clone the repository
git clone https://github.com/pletisan/giteagle.git
cd giteagle

# Install dependencies with uv
uv sync

# Run tests
uv run pytest

# Run linting
uv run ruff check src tests

# Run type checking
uv run mypy src
```

### Project Structure

```
giteagle/
├── src/giteagle/
│   ├── cli/              # CLI commands (Click + Rich)
│   ├── core/             # Core models and aggregation logic
│   ├── integrations/     # Platform API clients (GitHub, etc.)
│   └── config.py         # Configuration management
├── tests/
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
├── pyproject.toml        # Project configuration
└── uv.lock               # Locked dependencies
```

## Roadmap

- [ ] GitLab integration
- [ ] Bitbucket integration
- [ ] Web dashboard
- [ ] Slack/Discord notifications
- [ ] Custom activity filters
- [ ] Export to CSV/JSON
- [ ] Team/group analytics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`uv run pytest`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

Inspired by the challenges of managing multi-repository projects at scale. Built with:

- [Click](https://click.palletsprojects.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [httpx](https://www.python-httpx.org/) - Async HTTP client
- [Pydantic](https://docs.pydantic.dev/) - Data validation
