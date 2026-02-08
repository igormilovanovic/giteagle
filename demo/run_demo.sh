#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_FILE="$SCRIPT_DIR/DEMO.md"

cd "$PROJECT_ROOT"

# Kubernetes repos used in the demo
K8S_CORE="kubernetes/kubernetes"
K8S_MINIKUBE="kubernetes/minikube"
K8S_INGRESS="kubernetes/ingress-nginx"

TIMESTAMP="$(date -u '+%Y-%m-%d %H:%M:%S UTC')"

# --- Prerequisite checks ---

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
    echo "ERROR: GITHUB_TOKEN environment variable is not set."
    echo "Set it with: export GITHUB_TOKEN=ghp_your_token_here"
    exit 1
fi

if ! uv run giteagle --version >/dev/null 2>&1; then
    echo "ERROR: Cannot run 'uv run giteagle'. Ensure you have run 'uv sync' first."
    exit 1
fi

# --- Helper ---

strip_ansi() {
    sed $'s/\x1b\\[[0-9;]*[a-zA-Z]//g'
}

strip_uv_warnings() {
    grep -v '^warning: `VIRTUAL_ENV='
}

run_demo_command() {
    local section_num="$1"
    local title="$2"
    local description="$3"
    local cmd="$4"

    echo "Running demo ${section_num}: ${title}..."

    {
        echo ""
        echo "## ${section_num}. ${title}"
        echo ""
        echo "${description}"
        echo ""
        echo '```bash'
        echo "$ ${cmd}"
        echo '```'
        echo ""
    } >> "$OUTPUT_FILE"

    local output
    local exit_code=0
    output=$(NO_COLOR=1 bash -c "${cmd}" 2>&1) || exit_code=$?

    output=$(printf '%s' "$output" | strip_ansi | strip_uv_warnings)

    if [[ $exit_code -ne 0 ]]; then
        {
            echo '```'
            echo "Command failed with exit code ${exit_code}:"
            echo ""
            echo "${output}"
            echo '```'
            echo ""
        } >> "$OUTPUT_FILE"
        echo "  WARNING: Command failed (exit code ${exit_code}), continuing..."
    else
        {
            echo '```'
            echo "${output}"
            echo '```'
            echo ""
        } >> "$OUTPUT_FILE"
        echo "  Done."
    fi
}

# --- Write header ---

cat > "$OUTPUT_FILE" << HEADER
# Giteagle Demo: Kubernetes Ecosystem

> **Generated on ${TIMESTAMP}**
>
> This demo showcases giteagle by querying real activity across the
> [Kubernetes](https://github.com/kubernetes) GitHub organization.
> All output below is live data from the GitHub API — nothing is pre-recorded or faked.

---
HEADER

# --- Demo scenarios ---

run_demo_command \
    "1" \
    "Show Configuration" \
    "Display the current giteagle configuration, including which platform tokens are configured." \
    "uv run giteagle config"

run_demo_command \
    "2" \
    "List Kubernetes Organization Repos" \
    "List public repositories in the Kubernetes GitHub organization." \
    "uv run giteagle repos kubernetes --org"

run_demo_command \
    "3" \
    "Recent Activity on kubernetes/kubernetes" \
    "Show the 15 most recent activities (commits, pull requests, issues) from the core Kubernetes repository over the last 7 days." \
    "uv run giteagle activity ${K8S_CORE} --days 7 --limit 15"

run_demo_command \
    "4" \
    "Cross-Repository Summary" \
    "Aggregate activity across three Kubernetes repositories and break it down by type, top contributors, and per-repository counts." \
    "uv run giteagle summary ${K8S_CORE} ${K8S_MINIKUBE} ${K8S_INGRESS} --days 7"

run_demo_command \
    "5" \
    "Activity Timeline" \
    "Visualize weekly activity over the past 30 days across three Kubernetes repositories." \
    "uv run giteagle timeline ${K8S_CORE} ${K8S_MINIKUBE} ${K8S_INGRESS} --days 30 --granularity week"

# --- Footer ---

GITEAGLE_VERSION=$(NO_COLOR=1 uv run giteagle --version 2>/dev/null | strip_ansi || echo "unknown")

{
    echo "---"
    echo ""
    echo "*Demo completed at $(date -u '+%Y-%m-%d %H:%M:%S UTC').*"
    echo "*Run with ${GITEAGLE_VERSION}.*"
} >> "$OUTPUT_FILE"

echo ""
echo "Demo complete! Output written to: ${OUTPUT_FILE}"
