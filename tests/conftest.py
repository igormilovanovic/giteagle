"""Shared test fixtures."""

from datetime import datetime, timedelta

import pytest

from giteagle.core.models import Activity, ActivityType, Contributor, Repository


@pytest.fixture
def sample_contributor():
    """Create a sample contributor."""
    return Contributor(
        username="testuser",
        name="Test User",
        email="test@example.com",
        avatar_url="https://example.com/avatar.png",
    )


@pytest.fixture
def sample_repository():
    """Create a sample repository."""
    return Repository(
        name="test-repo",
        owner="testowner",
        platform="github",
        url="https://github.com/testowner/test-repo",
        description="A test repository",
        default_branch="main",
        is_private=False,
    )


@pytest.fixture
def sample_activity(sample_repository, sample_contributor):
    """Create a sample activity."""
    return Activity(
        id="test-activity-1",
        type=ActivityType.COMMIT,
        repository=sample_repository,
        contributor=sample_contributor,
        timestamp=datetime.now(),
        title="Test commit",
        description="This is a test commit",
        url="https://github.com/testowner/test-repo/commit/abc123",
    )


@pytest.fixture
def sample_activities(sample_repository, sample_contributor):
    """Create a list of sample activities."""
    base_time = datetime.now()
    activities = []

    # Create commits
    for i in range(5):
        activities.append(
            Activity(
                id=f"commit-{i}",
                type=ActivityType.COMMIT,
                repository=sample_repository,
                contributor=sample_contributor,
                timestamp=base_time - timedelta(hours=i),
                title=f"Commit {i}",
            )
        )

    # Create PRs
    for i in range(3):
        activities.append(
            Activity(
                id=f"pr-{i}",
                type=ActivityType.PULL_REQUEST,
                repository=sample_repository,
                contributor=Contributor(username=f"user{i}", name=f"User {i}"),
                timestamp=base_time - timedelta(hours=i + 5),
                title=f"PR {i}",
            )
        )

    # Create issues
    for i in range(2):
        activities.append(
            Activity(
                id=f"issue-{i}",
                type=ActivityType.ISSUE,
                repository=sample_repository,
                contributor=sample_contributor,
                timestamp=base_time - timedelta(hours=i + 8),
                title=f"Issue {i}",
            )
        )

    return activities


@pytest.fixture
def multiple_repos():
    """Create multiple sample repositories."""
    return [
        Repository(
            name="repo-1",
            owner="org1",
            platform="github",
            url="https://github.com/org1/repo-1",
        ),
        Repository(
            name="repo-2",
            owner="org1",
            platform="github",
            url="https://github.com/org1/repo-2",
        ),
        Repository(
            name="repo-3",
            owner="org2",
            platform="github",
            url="https://github.com/org2/repo-3",
        ),
    ]
