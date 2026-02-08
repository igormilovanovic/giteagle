"""Tests for GitHub API integration."""

from datetime import datetime
from unittest import mock

import httpx
import pytest

from giteagle.core.models import Repository
from giteagle.integrations.github import GitHubAPIError, GitHubClient, RateLimitError


class TestGitHubClient:
    """Tests for the GitHubClient class."""

    @pytest.fixture
    def mock_client(self):
        """Create a client with mocked HTTP transport."""
        return GitHubClient(token="test-token")

    @pytest.mark.asyncio
    async def test_client_initialization_with_token(self):
        """Test client initialization with a token."""
        client = GitHubClient(token="test-token")

        assert client.platform_name == "github"
        assert "Authorization" in client._client.headers
        await client.close()

    @pytest.mark.asyncio
    async def test_client_initialization_without_token(self):
        """Test client initialization without a token."""
        client = GitHubClient()

        assert "Authorization" not in client._client.headers
        await client.close()

    @pytest.mark.asyncio
    async def test_parse_repository(self, mock_client):
        """Test parsing GitHub API response to Repository model."""
        api_response = {
            "name": "test-repo",
            "owner": {"login": "testowner"},
            "html_url": "https://github.com/testowner/test-repo",
            "description": "A test repository",
            "default_branch": "main",
            "private": False,
        }

        repo = mock_client._parse_repository(api_response)

        assert repo.name == "test-repo"
        assert repo.owner == "testowner"
        assert repo.platform == "github"
        assert str(repo.url) == "https://github.com/testowner/test-repo"
        assert repo.description == "A test repository"
        assert repo.default_branch == "main"
        assert repo.is_private is False

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_parse_contributor(self, mock_client):
        """Test parsing GitHub API user data to Contributor model."""
        api_response = {
            "login": "testuser",
            "name": "Test User",
            "email": "test@example.com",
            "avatar_url": "https://avatars.example.com/testuser",
        }

        contributor = mock_client._parse_contributor(api_response)

        assert contributor.username == "testuser"
        assert contributor.name == "Test User"
        assert contributor.email == "test@example.com"
        assert contributor.avatar_url == "https://avatars.example.com/testuser"

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test using client as async context manager."""
        async with GitHubClient(token="test-token") as client:
            assert client.platform_name == "github"

    @pytest.mark.asyncio
    async def test_get_repository(self, mock_client):
        """Test fetching a repository."""
        mock_response = httpx.Response(
            200,
            json={
                "name": "test-repo",
                "owner": {"login": "testowner"},
                "html_url": "https://github.com/testowner/test-repo",
                "description": "A test repository",
                "default_branch": "main",
                "private": False,
            },
        )

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            repo = await mock_client.get_repository("testowner", "test-repo")

        assert repo.name == "test-repo"
        assert repo.owner == "testowner"

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_get_repository_not_found(self, mock_client):
        """Test handling 404 response."""
        mock_response = httpx.Response(404, json={"message": "Not Found"})

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            with pytest.raises(GitHubAPIError) as exc_info:
                await mock_client.get_repository("testowner", "nonexistent")

        assert exc_info.value.status_code == 404

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_rate_limit_detection(self, mock_client):
        """Test detection of rate limiting."""
        mock_response = httpx.Response(
            403,
            headers={
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": "1700000000",
            },
            json={"message": "Rate limit exceeded"},
        )

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            with pytest.raises(RateLimitError) as exc_info:
                await mock_client.get_repository("testowner", "test-repo")

        assert exc_info.value.reset_at is not None

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_list_repositories_user(self, mock_client):
        """Test listing repositories for a user."""
        mock_response = httpx.Response(
            200,
            json=[
                {
                    "name": "repo1",
                    "owner": {"login": "testuser"},
                    "html_url": "https://github.com/testuser/repo1",
                    "description": "First repo",
                    "default_branch": "main",
                    "private": False,
                },
                {
                    "name": "repo2",
                    "owner": {"login": "testuser"},
                    "html_url": "https://github.com/testuser/repo2",
                    "description": "Second repo",
                    "default_branch": "main",
                    "private": True,
                },
            ],
        )

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            repos = await mock_client.list_repositories(owner="testuser")

        assert len(repos) == 2
        assert repos[0].name == "repo1"
        assert repos[1].name == "repo2"

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_get_commits(self, mock_client):
        """Test fetching commits for a repository."""
        repo = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )

        mock_response = httpx.Response(
            200,
            json=[
                {
                    "sha": "abc123",
                    "commit": {
                        "message": "Test commit message",
                        "author": {
                            "name": "Test User",
                            "email": "test@example.com",
                            "date": "2024-01-15T10:30:00Z",
                        },
                    },
                    "author": {
                        "login": "testuser",
                        "avatar_url": "https://avatars.example.com/testuser",
                    },
                    "html_url": "https://github.com/testowner/test-repo/commit/abc123",
                },
            ],
        )

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            activities = await mock_client.get_commits(repo)

        assert len(activities) == 1
        assert activities[0].title == "Test commit message"
        assert activities[0].contributor.username == "testuser"
        assert activities[0].metadata["sha"] == "abc123"

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_get_pull_requests(self, mock_client):
        """Test fetching pull requests for a repository."""
        repo = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )

        mock_response = httpx.Response(
            200,
            json=[
                {
                    "number": 42,
                    "title": "Add new feature",
                    "body": "This PR adds a new feature",
                    "state": "open",
                    "user": {"login": "contributor"},
                    "html_url": "https://github.com/testowner/test-repo/pull/42",
                    "created_at": "2024-01-15T10:30:00Z",
                    "updated_at": "2024-01-15T11:00:00Z",
                },
            ],
        )

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            activities = await mock_client.get_pull_requests(repo)

        assert len(activities) == 1
        assert activities[0].title == "Add new feature"
        assert activities[0].contributor.username == "contributor"
        assert activities[0].metadata["number"] == 42

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_get_issues(self, mock_client):
        """Test fetching issues for a repository."""
        repo = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )

        mock_response = httpx.Response(
            200,
            json=[
                {
                    "number": 10,
                    "title": "Bug report",
                    "body": "Something is broken",
                    "state": "open",
                    "user": {"login": "reporter"},
                    "html_url": "https://github.com/testowner/test-repo/issues/10",
                    "created_at": "2024-01-15T10:30:00Z",
                    "updated_at": "2024-01-15T11:00:00Z",
                    "labels": [{"name": "bug"}],
                },
                {
                    "number": 11,
                    "title": "PR as issue",
                    "pull_request": {},  # This should be filtered out
                    "user": {"login": "reporter"},
                    "created_at": "2024-01-15T10:30:00Z",
                    "updated_at": "2024-01-15T11:00:00Z",
                },
            ],
        )

        with mock.patch.object(mock_client._client, "request", return_value=mock_response):
            activities = await mock_client.get_issues(repo)

        # Should only include actual issues, not PRs
        assert len(activities) == 1
        assert activities[0].title == "Bug report"
        assert activities[0].metadata["labels"] == ["bug"]

        await mock_client.close()

    @pytest.mark.asyncio
    async def test_get_activities_combines_all_types(self, mock_client):
        """Test that get_activities combines commits, PRs, and issues."""
        repo = Repository(
            name="test-repo",
            owner="testowner",
            platform="github",
            url="https://github.com/testowner/test-repo",
        )

        commit_response = [
            {
                "sha": "abc123",
                "commit": {
                    "message": "A commit",
                    "author": {"name": "Test", "date": "2024-01-15T12:00:00Z"},
                },
                "author": {"login": "testuser"},
                "html_url": "https://example.com/commit/abc123",
            },
        ]

        pr_response = [
            {
                "number": 1,
                "title": "A PR",
                "state": "open",
                "user": {"login": "testuser"},
                "html_url": "https://example.com/pull/1",
                "created_at": "2024-01-15T11:00:00Z",
                "updated_at": "2024-01-15T11:00:00Z",
            },
        ]

        issue_response = [
            {
                "number": 2,
                "title": "An issue",
                "state": "open",
                "user": {"login": "testuser"},
                "html_url": "https://example.com/issues/2",
                "created_at": "2024-01-15T10:00:00Z",
                "updated_at": "2024-01-15T10:00:00Z",
            },
        ]

        call_count = 0

        def mock_request(*args, **kwargs):
            nonlocal call_count
            path = args[1] if len(args) > 1 else kwargs.get("path", "")

            if "commits" in path:
                return httpx.Response(200, json=commit_response)
            elif "pulls" in path:
                return httpx.Response(200, json=pr_response)
            elif "issues" in path:
                return httpx.Response(200, json=issue_response)

            return httpx.Response(200, json=[])

        with mock.patch.object(mock_client._client, "request", side_effect=mock_request):
            activities = await mock_client.get_activities(repo)

        assert len(activities) == 3

        await mock_client.close()


class TestGitHubAPIError:
    """Tests for GitHubAPIError."""

    def test_error_with_message(self):
        """Test creating an error with just a message."""
        error = GitHubAPIError("Something went wrong")

        assert str(error) == "Something went wrong"
        assert error.status_code == 0
        assert error.response == {}

    def test_error_with_all_fields(self):
        """Test creating an error with all fields."""
        error = GitHubAPIError(
            "Not Found",
            status_code=404,
            response={"message": "Not Found", "documentation_url": "https://docs.github.com"},
        )

        assert str(error) == "Not Found"
        assert error.status_code == 404
        assert error.response["documentation_url"] == "https://docs.github.com"


class TestRateLimitError:
    """Tests for RateLimitError."""

    def test_rate_limit_error(self):
        """Test creating a rate limit error."""
        reset_at = datetime(2024, 1, 15, 12, 0, 0)
        error = RateLimitError(reset_at)

        assert str(error) == "Rate limit exceeded"
        assert error.status_code == 403
        assert error.reset_at == reset_at
