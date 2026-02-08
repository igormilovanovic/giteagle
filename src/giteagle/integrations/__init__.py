"""Platform integrations for fetching repository data."""

from giteagle.integrations.base import PlatformClient
from giteagle.integrations.github import GitHubClient

__all__ = [
    "PlatformClient",
    "GitHubClient",
]
