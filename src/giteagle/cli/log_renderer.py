"""Log renderer for multi-repo git log visualization."""

from __future__ import annotations

from itertools import groupby

from rich.console import Console

from giteagle.core.models import Activity

REPO_COLORS: list[str] = [
    "cyan",
    "magenta",
    "green",
    "yellow",
    "blue",
    "red",
    "bright_cyan",
    "bright_magenta",
    "bright_green",
    "bright_yellow",
]


def assign_repo_colors(repo_names: list[str]) -> dict[str, str]:
    """Assign a distinct color to each repository name."""
    return {name: REPO_COLORS[i % len(REPO_COLORS)] for i, name in enumerate(sorted(repo_names))}


def get_display_names(repo_full_names: list[str]) -> dict[str, str]:
    """Compute short display names, disambiguating when needed."""
    short_names: dict[str, list[str]] = {}
    for full_name in repo_full_names:
        short = full_name.split("/")[-1]
        short_names.setdefault(short, []).append(full_name)

    display: dict[str, str] = {}
    for short, full_list in short_names.items():
        if len(full_list) == 1:
            display[full_list[0]] = short
        else:
            for full in full_list:
                display[full] = full
    return display


def group_by_date(activities: list[Activity]) -> list[tuple[str, list[Activity]]]:
    """Group activities by date string, preserving order."""

    def date_key(a: Activity) -> str:
        return a.timestamp.strftime("%Y-%m-%d")

    groups: list[tuple[str, list[Activity]]] = []
    for key, group in groupby(activities, key=date_key):
        groups.append((key, list(group)))
    return groups


def render_log(
    console: Console,
    activities: list[Activity],
    repo_colors: dict[str, str],
    display_names: dict[str, str],
) -> None:
    """Render the multi-repo log to the console."""
    if not activities:
        console.print("[yellow]No commits found in the specified period.[/yellow]")
        return

    groups = group_by_date(activities)
    max_name_len = max(len(v) for v in display_names.values()) if display_names else 10

    for _group_idx, (date_str, day_activities) in enumerate(groups):
        for commit_idx, activity in enumerate(day_activities):
            repo_name = activity.repository.full_name
            color = repo_colors.get(repo_name, "white")
            label = display_names.get(repo_name, repo_name)
            sha = activity.metadata.get("sha", "???????")[:7]
            parents = activity.metadata.get("parents", [])
            message = activity.title

            if commit_idx == 0:
                graph = "[bold white]\u25cf[/bold white]"
                date_display = f"[dim]{date_str}[/dim]"
            else:
                graph = "[dim]\u2502[/dim]"
                date_display = " " * 10

            merge_marker = ""
            if len(parents) > 1:
                merge_marker = " [dim](merge)[/dim]"

            line = (
                f" {graph} {date_display}  "
                f"[{color}]{label:<{max_name_len}}[/{color}]  "
                f"[dim]{sha}[/dim]  "
                f"{message}{merge_marker}"
            )
            console.print(line)

    total = len(activities)
    repo_count = len(repo_colors)
    console.print(f"\n[dim]Total: {total} commits across {repo_count} repositories[/dim]")
