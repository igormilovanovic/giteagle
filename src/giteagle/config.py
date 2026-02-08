"""Configuration management for Giteagle."""

import os
from pathlib import Path
from typing import Any, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, SecretStr


class PlatformConfig(BaseModel):
    """Configuration for a single platform."""

    token: Optional[SecretStr] = Field(None, description="API token")
    base_url: Optional[str] = Field(None, description="Base API URL (for enterprise)")


class GiteagleConfig(BaseModel):
    """Main configuration for Giteagle."""

    model_config = ConfigDict(extra="ignore")

    github: PlatformConfig = Field(default_factory=PlatformConfig)
    gitlab: PlatformConfig = Field(default_factory=PlatformConfig)
    bitbucket: PlatformConfig = Field(default_factory=PlatformConfig)
    default_platform: str = Field("github", description="Default platform to use")
    cache_ttl: int = Field(300, description="Cache TTL in seconds")
    max_concurrent_requests: int = Field(10, description="Max concurrent API requests")


def get_config_path() -> Path:
    """Get the path to the configuration file."""
    # Check environment variable first
    if env_path := os.environ.get("GITEAGLE_CONFIG"):
        return Path(env_path)

    # Check XDG config directory
    xdg_config = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    xdg_path = Path(xdg_config) / "giteagle" / "config.yaml"
    if xdg_path.exists():
        return xdg_path

    # Check home directory
    home_path = Path.home() / ".giteagle.yaml"
    if home_path.exists():
        return home_path

    # Default to XDG location
    return xdg_path


def load_config(path: Optional[Path] = None) -> GiteagleConfig:
    """Load configuration from file and environment variables."""
    config_path = path or get_config_path()
    config_data: dict[str, Any] = {}

    # Load from file if exists
    if config_path.exists():
        with open(config_path) as f:
            config_data = yaml.safe_load(f) or {}

    # Override with environment variables
    if github_token := os.environ.get("GITHUB_TOKEN"):
        if "github" not in config_data:
            config_data["github"] = {}
        config_data["github"]["token"] = github_token

    if gitlab_token := os.environ.get("GITLAB_TOKEN"):
        if "gitlab" not in config_data:
            config_data["gitlab"] = {}
        config_data["gitlab"]["token"] = gitlab_token

    if bitbucket_token := os.environ.get("BITBUCKET_TOKEN"):
        if "bitbucket" not in config_data:
            config_data["bitbucket"] = {}
        config_data["bitbucket"]["token"] = bitbucket_token

    return GiteagleConfig(**config_data)


def save_config(config: GiteagleConfig, path: Optional[Path] = None) -> None:
    """Save configuration to file."""
    config_path = path or get_config_path()

    # Create directory if needed
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert to dict, handling SecretStr
    data = config.model_dump()
    for platform in ["github", "gitlab", "bitbucket"]:
        if data[platform]["token"]:
            data[platform]["token"] = data[platform]["token"].get_secret_value()

    with open(config_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False)
