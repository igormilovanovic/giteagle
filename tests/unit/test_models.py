"""Tests for core data models."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from giteagle.core.models import Activity, ActivityType, Contributor, Repository


class TestContributor:
    """Tests for the Contributor model."""

    def test_create_contributor_with_required_fields(self):
        """Test creating a contributor with only required fields."""
        contributor = Contributor(username="testuser")

        assert contributor.username == "testuser"
        assert contributor.name is None
        assert contributor.email is None
        assert contributor.avatar_url is None

    def test_create_contributor_with_all_fields(self):
        """Test creating a contributor with all fields."""
        contributor = Contributor(
            username="testuser",
            name="Test User",
            email="test@example.com",
            avatar_url="https://example.com/avatar.png",
        )

        assert contributor.username == "testuser"
        assert contributor.name == "Test User"
        assert contributor.email == "test@example.com"
        assert contributor.avatar_url == "https://example.com/avatar.png"

    def test_contributor_equality(self):
        """Test that contributors with same username are equal."""
        contrib1 = Contributor(username="testuser", name="User 1")
        contrib2 = Contributor(username="testuser", name="User 2")

        assert contrib1 == contrib2

    def test_contributor_inequality(self):
        """Test that contributors with different usernames are not equal."""
        contrib1 = Contributor(username="user1")
        contrib2 = Contributor(username="user2")

        assert contrib1 != contrib2

    def test_contributor_hash(self):
        """Test that contributors can be used in sets."""
        contrib1 = Contributor(username="testuser", name="User 1")
        contrib2 = Contributor(username="testuser", name="User 2")
        contrib3 = Contributor(username="otheruser")

        contributor_set = {contrib1, contrib2, contrib3}
        assert len(contributor_set) == 2

    def test_contributor_requires_username(self):
        """Test that username is required."""
        with pytest.raises(ValidationError):
            Contributor()


class TestRepository:
    """Tests for the Repository model."""

    def test_create_repository_with_required_fields(self):
        """Test creating a repository with required fields."""
        repo = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )

        assert repo.name == "test-repo"
        assert repo.owner == "testowner"
        assert repo.platform == "github"
        assert str(repo.url) == "https://github.com/testowner/test-repo"
        assert repo.default_branch == "main"
        assert repo.is_private is False

    def test_repository_full_name(self):
        """Test the full_name property."""
        repo = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )

        assert repo.full_name == "testowner/test-repo"

    def test_repository_equality(self):
        """Test that repositories with same platform/owner/name are equal."""
        repo1 = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
            description="Repo 1",
        )
        repo2 = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
            description="Repo 2",
        )

        assert repo1 == repo2

    def test_repository_inequality_different_platform(self):
        """Test that repositories on different platforms are not equal."""
        repo1 = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )
        repo2 = Repository(
            name="test-repo",
            owner="testowner",
            platform="gitlab",
            url="https://gitlab.com/testowner/test-repo",
        )

        assert repo1 != repo2

    def test_repository_hash(self):
        """Test that repositories can be used in sets."""
        repo1 = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )
        repo2 = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )
        repo3 = Repository(
            name="other-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/other-repo",
        )

        repo_set = {repo1, repo2, repo3}
        assert len(repo_set) == 2

    def test_repository_invalid_url(self):
        """Test that invalid URLs are rejected."""
        with pytest.raises(ValidationError):
            Repository(
                name="test-repo",
                owner="testowner",
                platform="github",
                url="not-a-valid-url",
            )


class TestActivityType:
    """Tests for the ActivityType enum."""

    def test_activity_types_exist(self):
        """Test that all expected activity types exist."""
        assert ActivityType.COMMIT == "commit"
        assert ActivityType.PULL_REQUEST == "pull_request"
        assert ActivityType.PULL_REQUEST_REVIEW == "pull_request_review"
        assert ActivityType.ISSUE == "issue"
        assert ActivityType.ISSUE_COMMENT == "issue_comment"
        assert ActivityType.RELEASE == "release"


class TestActivity:
    """Tests for the Activity model."""

    def test_create_activity(self, sample_repository, sample_contributor):
        """Test creating an activity."""
        now = datetime.now()
        activity = Activity(
            id="test-activity-1",
            type=ActivityType.COMMIT,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=now,
            title="Test commit",
            description="This is a test commit",
            url="https://github.com/testowner/test-repo/commit/abc123",
        )

        assert activity.id == "test-activity-1"
        assert activity.type == ActivityType.COMMIT
        assert activity.repository == sample_repository
        assert activity.contributor == sample_contributor
        assert activity.timestamp == now
        assert activity.title == "Test commit"
        assert activity.description == "This is a test commit"
        assert activity.metadata == {}

    def test_activity_with_metadata(self, sample_repository, sample_contributor):
        """Test creating an activity with metadata."""
        activity = Activity(
            id="test-activity-1",
            type=ActivityType.COMMIT,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=datetime.now(),
            title="Test commit",
            metadata={"sha": "abc123", "lines_added": 10},
        )

        assert activity.metadata == {"sha": "abc123", "lines_added": 10}

    def test_activity_equality(self, sample_repository, sample_contributor):
        """Test that activities with same ID are equal."""
        activity1 = Activity(
            id="test-activity-1",
            type=ActivityType.COMMIT,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=datetime.now(),
            title="Commit 1",
        )
        activity2 = Activity(
            id="test-activity-1",
            type=ActivityType.ISSUE,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=datetime.now(),
            title="Issue 1",
        )

        assert activity1 == activity2

    def test_activity_hash(self, sample_repository, sample_contributor):
        """Test that activities can be used in sets."""
        activity1 = Activity(
            id="activity-1",
            type=ActivityType.COMMIT,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=datetime.now(),
            title="Activity 1",
        )
        activity2 = Activity(
            id="activity-1",
            type=ActivityType.COMMIT,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=datetime.now(),
            title="Activity 1 duplicate",
        )
        activity3 = Activity(
            id="activity-2",
            type=ActivityType.COMMIT,
            repository=sample_repository,
            contributor=sample_contributor,
            timestamp=datetime.now(),
            title="Activity 2",
        )

        activity_set = {activity1, activity2, activity3}
        assert len(activity_set) == 2
