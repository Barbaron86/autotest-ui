import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.regression
def test_allure_log_attachments_are_isolated() -> None:
    test_workspace = PROJECT_ROOT / f".allure-log-test-{uuid4().hex}"
    test_workspace.mkdir()

    (test_workspace / "conftest.py").write_text(
        """
from pytest import Config

from tools.logger import configure_logging

pytest_plugins = ("tools.allure.logs",)


def pytest_configure(config: Config) -> None:
    configure_logging()
""".strip(),
        encoding="utf-8",
    )
    (test_workspace / "test_logging.py").write_text(
        """
import pytest
from loguru import logger


@pytest.fixture(scope="session", autouse=True)
def session_resource():
    logger.bind(component="SESSION").info("SESSION_SETUP_MESSAGE")
    yield
    logger.bind(component="SESSION").info("SESSION_TEARDOWN_MESSAGE")


def test_first() -> None:
    logger.bind(component="FIRST").info("FIRST_UNIQUE_MESSAGE")


def test_second() -> None:
    logger.bind(component="SECOND").warning("SECOND_UNIQUE_MESSAGE")
""".strip(),
        encoding="utf-8",
    )

    allure_results = test_workspace / "allure-results"
    command = [
        sys.executable,
        "-m",
        "pytest",
        str(test_workspace / "test_logging.py"),
        "-q",
        "-s",
        "-p",
        "no:cacheprovider",
        "--confcutdir",
        str(test_workspace),
        "--alluredir",
        str(allure_results),
        "--clean-alluredir",
    ]
    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"
    environment["PYTHONPATH"] = os.pathsep.join(filter(None, (str(PROJECT_ROOT), environment.get("PYTHONPATH"))))
    try:
        completed = subprocess.run(
            command,
            cwd=test_workspace,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
            check=False,
            timeout=60,
        )

        assert completed.returncode == 0, completed.stdout + completed.stderr
        assert "💡 INFO" in completed.stderr
        assert "⚠️ WARNING" in completed.stderr

        attachments: dict[str, str] = {}
        for result_file in allure_results.glob("*-result.json"):
            result = json.loads(result_file.read_text(encoding="utf-8"))
            test_logs = [attachment for attachment in result["attachments"] if attachment["name"] == "Test log"]

            assert len(test_logs) == 1
            attachment_file = allure_results / test_logs[0]["source"]
            attachments[result["name"]] = attachment_file.read_text(encoding="utf-8")

        assert attachments.keys() == {"test_first", "test_second"}
        assert "FIRST_UNIQUE_MESSAGE" in attachments["test_first"]
        assert "SESSION_SETUP_MESSAGE" in attachments["test_first"]
        assert "SESSION_TEARDOWN_MESSAGE" not in attachments["test_first"]
        assert "SECOND_UNIQUE_MESSAGE" not in attachments["test_first"]
        assert "SECOND_UNIQUE_MESSAGE" in attachments["test_second"]
        assert "SESSION_TEARDOWN_MESSAGE" in attachments["test_second"]
        assert "SESSION_SETUP_MESSAGE" not in attachments["test_second"]
        assert "FIRST_UNIQUE_MESSAGE" not in attachments["test_second"]
        assert all("\x1b[" not in test_log for test_log in attachments.values())
    finally:
        shutil.rmtree(test_workspace)
