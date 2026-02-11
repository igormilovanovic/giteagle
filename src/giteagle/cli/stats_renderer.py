"""DORA-style PR metrics renderer for cross-repo analysis."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

from rich import box
from rich.console import Console
from rich.table import Table


@dataclass
class PRMetrics:
    """Metrics for a single merged PR."""

    repo_name: str
    number: int
    title: str
    created_at: datetime
    merged_at: datetime
    first_review_at: datetime | None
    time_to_merge: timedelta
    time_to_first_review: timedelta | None


@dataclass
class RepoStats:
    """Aggregated metrics for one repository."""

    repo_name: str
    merged_count: int
    closed_count: int
    median_time_to_merge: timedelta
    median_time_to_first_review: timedelta | None
    merge_rate: float
    throughput_per_week: float


def median_timedelta(deltas: list[timedelta]) -> timedelta:
    """Compute the median of a list of timedeltas."""
    if not deltas:
        return timedelta(0)
    sorted_deltas = sorted(deltas)
    mid = len(sorted_deltas) // 2
    if len(sorted_deltas) % 2 == 0:
        return (sorted_deltas[mid - 1] + sorted_deltas[mid]) / 2
    return sorted_deltas[mid]


def format_duration(td: timedelta) -> str:
    """Format timedelta as human-readable: '2d 3h', '45m', '1w 2d'."""
    total_seconds = int(td.total_seconds())
    if total_seconds < 0:
        return "0m"

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    if days >= 7:
        weeks = days // 7
        remaining_days = days % 7
        if remaining_days > 0:
            return f"{weeks}w {remaining_days}d"
        return f"{weeks}w"
    if days > 0:
        if hours > 0:
            return f"{days}d {hours}h"
        return f"{days}d"
    if hours > 0:
        if minutes > 0:
            return f"{hours}h {minutes}m"
        return f"{hours}h"
    return f"{max(minutes, 1)}m"


def build_pr_metrics(
    raw_prs: list[dict],
    reviews_map: dict[int, list[dict]],
    repo_name: str,
) -> list[PRMetrics]:
    """Convert raw API data into PRMetrics objects for merged PRs."""
    metrics: list[PRMetrics] = []
    for pr in raw_prs:
        merged_at_str = pr.get("merged_at")
        if not merged_at_str:
            continue

        created_at = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
        merged_at = datetime.fromisoformat(merged_at_str.replace("Z", "+00:00"))

        # Find first review timestamp (excluding COMMENTED-only)
        reviews = reviews_map.get(pr["number"], [])
        first_review_at: datetime | None = None
        for review in sorted(reviews, key=lambda r: r.get("submitted_at", "")):
            state = review.get("state", "")
            if state in ("APPROVED", "CHANGES_REQUESTED", "DISMISSED"):
                submitted = review.get("submitted_at")
                if submitted:
                    first_review_at = datetime.fromisoformat(submitted.replace("Z", "+00:00"))
                    break

        time_to_merge = merged_at - created_at
        time_to_first_review = (first_review_at - created_at) if first_review_at else None

        metrics.append(
            PRMetrics(
                repo_name=repo_name,
                number=pr["number"],
                title=pr.get("title", ""),
                created_at=created_at,
                merged_at=merged_at,
                first_review_at=first_review_at,
                time_to_merge=time_to_merge,
                time_to_first_review=time_to_first_review,
            )
        )
    return metrics


def compute_repo_stats(
    metrics: list[PRMetrics],
    closed_count: int,
    repo_name: str,
    *,
    window_days: int,
) -> RepoStats:
    """Compute aggregate stats for a repo."""
    merged_count = len(metrics)

    ttm_deltas = [m.time_to_merge for m in metrics]
    ttfr_deltas = [m.time_to_first_review for m in metrics if m.time_to_first_review is not None]

    median_ttm = median_timedelta(ttm_deltas)
    median_ttfr = median_timedelta(ttfr_deltas) if ttfr_deltas else None

    merge_rate = merged_count / closed_count if closed_count > 0 else 0.0
    weeks = max(window_days / 7, 1)
    throughput = merged_count / weeks

    return RepoStats(
        repo_name=repo_name,
        merged_count=merged_count,
        closed_count=closed_count,
        median_time_to_merge=median_ttm,
        median_time_to_first_review=median_ttfr,
        merge_rate=merge_rate,
        throughput_per_week=throughput,
    )


def compute_trend(current: float, previous: float, *, threshold: float = 0.1) -> str:
    """Compute trend indicator: 'up', 'down', or 'stable'."""
    if previous == 0:
        return "n/a"
    change = (current - previous) / previous
    if change > threshold:
        return "up"
    if change < -threshold:
        return "down"
    return "stable"


def _trend_indicator(trend: str) -> str:
    """Return a styled trend indicator for Rich output."""
    if trend == "up":
        return "[green]^ up[/green]"
    if trend == "down":
        return "[red]v down[/red]"
    if trend == "stable":
        return "[dim]= stable[/dim]"
    return "[dim]--[/dim]"


def render_stats(
    console: Console,
    current_stats: list[RepoStats],
    previous_stats: list[RepoStats],
    *,
    window_days: int,
) -> None:
    """Render DORA-style metrics table."""
    if not current_stats:
        console.print("[yellow]No merged pull requests found in the specified period.[/yellow]")
        return

    prev_map = {s.repo_name: s for s in previous_stats}

    table = Table(title=f"PR Metrics (last {window_days} days)", box=box.ROUNDED)
    table.add_column("Repo", style="cyan", no_wrap=True)
    table.add_column("Merged", justify="right")
    table.add_column("Median TTM", no_wrap=True)
    table.add_column("Median TTFR", no_wrap=True)
    table.add_column("Merge Rate", justify="right")
    table.add_column("PRs/week", no_wrap=True)

    total_merged = 0
    total_closed = 0
    all_ttm: list[timedelta] = []
    all_ttfr: list[timedelta] = []

    for stats in current_stats:
        total_merged += stats.merged_count
        total_closed += stats.closed_count

        prev = prev_map.get(stats.repo_name)
        throughput_trend = (
            compute_trend(stats.throughput_per_week, prev.throughput_per_week) if prev else "n/a"
        )

        ttm_str = format_duration(stats.median_time_to_merge)
        ttfr_str = (
            format_duration(stats.median_time_to_first_review)
            if stats.median_time_to_first_review
            else "[dim]--[/dim]"
        )
        rate_str = f"{stats.merge_rate:.0%}"

        table.add_row(
            stats.repo_name.split("/")[-1],
            str(stats.merged_count),
            ttm_str,
            ttfr_str,
            rate_str,
            f"{stats.throughput_per_week:.1f}  {_trend_indicator(throughput_trend)}",
        )

    # Overall row if multiple repos
    if len(current_stats) > 1:
        # Collect all individual metrics for overall calculation
        for stats in current_stats:
            all_ttm.append(stats.median_time_to_merge)
            if stats.median_time_to_first_review:
                all_ttfr.append(stats.median_time_to_first_review)

        overall_ttm = median_timedelta(all_ttm)
        overall_ttfr = median_timedelta(all_ttfr) if all_ttfr else None
        overall_rate = total_merged / total_closed if total_closed > 0 else 0.0
        weeks = max(window_days / 7, 1)
        overall_throughput = total_merged / weeks

        table.add_section()
        table.add_row(
            "[bold]Overall[/bold]",
            f"[bold]{total_merged}[/bold]",
            f"[bold]{format_duration(overall_ttm)}[/bold]",
            f"[bold]{format_duration(overall_ttfr)}[/bold]" if overall_ttfr else "[dim]--[/dim]",
            f"[bold]{overall_rate:.0%}[/bold]",
            f"[bold]{overall_throughput:.1f}[/bold]",
        )

    console.print(table)
