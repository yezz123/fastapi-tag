import subprocess
from unittest.mock import MagicMock, patch

import pytest

from fastapi_tag.metadata import read_app_version


@pytest.fixture
def mock_file_content():
    return "1.0.0"


def test_read_app_version_from_file(mock_file_content):
    with patch(
        "builtins.open",
        return_value=MagicMock(read=MagicMock(return_value=mock_file_content)),
    ):
        assert read_app_version() == mock_file_content


def test_read_app_version_from_git(mock_file_content):
    with patch(
        "subprocess.run",
        return_value=MagicMock(
            stdout=MagicMock(decode=MagicMock(return_value=mock_file_content))
        ),
    ):
        assert read_app_version() == mock_file_content


def test_read_app_version_default():
    with patch("builtins.open", side_effect=FileNotFoundError), patch(
        "subprocess.run", side_effect=subprocess.SubprocessError
    ):
        assert read_app_version() == "1.0.0"


def test_read_app_version_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError), patch(
        "subprocess.run",
        return_value=MagicMock(stdout=MagicMock(decode=MagicMock(return_value=""))),
    ):
        assert read_app_version() == "1.0.0"


def test_read_app_version_subprocess_error():
    with patch(
        "builtins.open", return_value=MagicMock(read=MagicMock(return_value=""))
    ), patch("subprocess.run", side_effect=subprocess.SubprocessError):
        assert read_app_version() == "1.0.0"


def test_read_app_version_git_command_not_found():
    with patch(
        "builtins.open", return_value=MagicMock(read=MagicMock(return_value=""))
    ), patch("subprocess.run", side_effect=FileNotFoundError):
        assert read_app_version() == "1.0.0"
