"""Tests for configuration management."""

import os
from unittest import mock

import pytest
import yaml

from giteagle.config import (
    GiteagleConfig,
    PlatformConfig,
    get_config_path,
    load_config,
    save_config,
)


class TestPlatformConfig:
    """Tests for PlatformConfig."""

    def test_create_empty_platform_config(self):
        """Test creating an empty platform config."""
        config = PlatformConfig()

        assert config.token is None
        assert config.base_url is None

    def test_create_platform_config_with_token(self):
        """Test creating a platform config with a token."""
        config = PlatformConfig(token="test-token")

        assert config.token is not None
        assert config.token.get_secret_value() == "test-token"

    def test_base_url_rejects_http(self):
        """Test that base_url rejects non-HTTPS schemes."""
        with pytest.raises(ValueError, match="must use HTTPS"):
            PlatformConfig(base_url="http://evil.example.com")

    def test_base_url_accepts_https(self):
        """Test that base_url accepts HTTPS URLs."""
        config = PlatformConfig(base_url="https://github.example.com/api/v3")
        assert config.base_url == "https://github.example.com/api/v3"

    def test_base_url_rejects_no_hostname(self):
        """Test that base_url rejects URLs without a hostname."""
        with pytest.raises(ValueError, match="valid hostname"):
            PlatformConfig(base_url="https://")

    def test_base_url_accepts_none(self):
        """Test that base_url accepts None."""
        config = PlatformConfig(base_url=None)
        assert config.base_url is None


class TestGiteagleConfig:
    """Tests for the main GiteagleConfig class."""

    def test_create_default_config(self):
        """Test creating a config with defaults."""
        config = GiteagleConfig()

        assert config.default_platform == "github"
        assert config.cache_ttl == 300
        assert config.max_concurrent_requests == 10
        assert config.github.token is None
        assert config.gitlab.token is None
        assert config.bitbucket.token is None

    def test_create_config_with_values(self):
        """Test creating a config with custom values."""
        config = GiteagleConfig(
            default_platform="gitlab",
            cache_ttl=600,
            max_concurrent_requests=20,
            github=PlatformConfig(token="gh-token"),
        )

        assert config.default_platform == "gitlab"
        assert config.cache_ttl == 600
        assert config.max_concurrent_requests == 20
        assert config.github.token.get_secret_value() == "gh-token"


class TestGetConfigPath:
    """Tests for get_config_path function."""

    def test_returns_env_var_path_if_set(self, tmp_path):
        """Test that GITEAGLE_CONFIG env var is respected."""
        config_file = tmp_path / "custom-config.yaml"
        config_file.touch()

        with mock.patch.dict(os.environ, {"GITEAGLE_CONFIG": str(config_file)}):
            path = get_config_path()

        assert path == config_file

    def test_returns_xdg_path_if_exists(self, tmp_path):
        """Test that XDG config path is used if it exists."""
        xdg_config = tmp_path / ".config"
        config_dir = xdg_config / "giteagle"
        config_dir.mkdir(parents=True)
        config_file = config_dir / "config.yaml"
        config_file.touch()

        with mock.patch.dict(
            os.environ,
            {
                "XDG_CONFIG_HOME": str(xdg_config),
                "GITEAGLE_CONFIG": "",
            },
            clear=False,
        ):
            # Remove GITEAGLE_CONFIG if set
            os.environ.pop("GITEAGLE_CONFIG", None)
            path = get_config_path()

        assert path == config_file


class TestLoadConfig:
    """Tests for load_config function."""

    def test_load_config_from_file(self, tmp_path):
        """Test loading config from a YAML file."""
        config_file = tmp_path / "config.yaml"
        config_data = {
            "default_platform": "gitlab",
            "cache_ttl": 600,
            "github": {"token": "gh-token-from-file"},
        }
        with open(config_file, "w") as f:
            yaml.dump(config_data, f)

        config = load_config(config_file)

        assert config.default_platform == "gitlab"
        assert config.cache_ttl == 600
        assert config.github.token.get_secret_value() == "gh-token-from-file"

    def test_load_config_env_override(self, tmp_path):
        """Test that env vars override file config."""
        config_file = tmp_path / "config.yaml"
        config_data = {
            "github": {"token": "file-token"},
        }
        with open(config_file, "w") as f:
            yaml.dump(config_data, f)

        with mock.patch.dict(os.environ, {"GITHUB_TOKEN": "env-token"}):
            config = load_config(config_file)

        assert config.github.token.get_secret_value() == "env-token"

    def test_load_config_nonexistent_file(self, tmp_path):
        """Test loading from a nonexistent file returns defaults."""
        config_file = tmp_path / "nonexistent.yaml"

        config = load_config(config_file)

        assert config.default_platform == "github"
        assert config.github.token is None

    def test_load_config_gitlab_token_from_env(self, tmp_path):
        """Test loading GitLab token from environment."""
        config_file = tmp_path / "config.yaml"
        config_file.touch()

        with mock.patch.dict(os.environ, {"GITLAB_TOKEN": "gitlab-token"}):
            config = load_config(config_file)

        assert config.gitlab.token.get_secret_value() == "gitlab-token"

    def test_load_config_bitbucket_token_from_env(self, tmp_path):
        """Test loading Bitbucket token from environment."""
        config_file = tmp_path / "config.yaml"
        config_file.touch()

        with mock.patch.dict(os.environ, {"BITBUCKET_TOKEN": "bb-token"}):
            config = load_config(config_file)

        assert config.bitbucket.token.get_secret_value() == "bb-token"

    def test_load_config_empty_file(self, tmp_path):
        """Test loading from an empty file returns defaults."""
        config_file = tmp_path / "empty.yaml"
        config_file.touch()

        config = load_config(config_file)

        assert config.default_platform == "github"


class TestSaveConfig:
    """Tests for save_config function."""

    def test_save_config_creates_file(self, tmp_path):
        """Test that save_config creates the config file."""
        config_file = tmp_path / "subdir" / "config.yaml"
        config = GiteagleConfig(default_platform="gitlab", cache_ttl=600)

        save_config(config, config_file)

        assert config_file.exists()

    def test_save_config_preserves_values(self, tmp_path):
        """Test that saved config can be loaded back."""
        config_file = tmp_path / "config.yaml"
        original = GiteagleConfig(
            default_platform="gitlab",
            cache_ttl=600,
            github=PlatformConfig(token="test-token"),
        )

        save_config(original, config_file)
        loaded = load_config(config_file)

        assert loaded.default_platform == "gitlab"
        assert loaded.cache_ttl == 600
        assert loaded.github.token.get_secret_value() == "test-token"

    def test_save_config_handles_none_tokens(self, tmp_path):
        """Test saving config with no tokens set."""
        config_file = tmp_path / "config.yaml"
        config = GiteagleConfig()

        save_config(config, config_file)

        # Should not raise an error
        with open(config_file) as f:
            data = yaml.safe_load(f)

        assert data["github"]["token"] is None

    def test_save_config_sets_restrictive_permissions(self, tmp_path):
        """Test that saved config file has owner-only permissions."""
        config_file = tmp_path / "config.yaml"
        config = GiteagleConfig(github=PlatformConfig(token="secret"))

        save_config(config, config_file)

        file_stat = config_file.stat()
        mode = file_stat.st_mode & 0o777
        assert mode == 0o600, f"Expected 0o600 permissions, got {oct(mode)}"
