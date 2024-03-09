import logging
import subprocess
from functools import lru_cache as cache

log = logging.getLogger(__name__)


@cache(maxsize=1)
def read_app_version():
    """Attempts to read the version from the environment, returning 'NA' when it
    fails.  It first looks for the existence of a VERSION file, then tries to
    use git to obtain a tag.
    """
    return _read_version_from_file() or _read_version_from_git() or "NA"


def _read_version_from_file():
    """
    :returns: A string describing the version.
    """
    handle = None
    try:
        handle = open("VERSION", "r")
        version = handle.read().rstrip()
        log.info("Read version from file")
        return version
    except FileNotFoundError:
        return None
    finally:
        if handle:
            handle.close()


def _read_version_from_git():
    """
    :returns: A string describing the version.
    """
    try:
        version = (
            subprocess.run(
                ["git", "describe", "--always", "--tags"],
                stdout=subprocess.PIPE,
                check=False,
            )
            .stdout.decode("utf-8")
            .rstrip()
        )
        log.info("Read version from git")
        return version
    except subprocess.SubprocessError:
        return None
    except FileNotFoundError:
        return None
