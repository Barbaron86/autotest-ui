from collections.abc import Generator
from dataclasses import dataclass
from io import StringIO

import allure
import pytest
from loguru import logger
from pluggy import Result
from pytest import Item, TestReport

_ALLURE_LOG_FORMAT = "{time:HH:mm:ss.SSS} | {level.icon} {level: <8} | {extra[component]: <14} | {message}"


@dataclass(frozen=True, slots=True)
class _LogCapture:
    buffer: StringIO
    handler_id: int


_LOG_CAPTURE_KEY = pytest.StashKey[_LogCapture]()


def _stop_log_capture(item: Item) -> str | None:
    capture = item.stash.get(_LOG_CAPTURE_KEY, None)
    if capture is None:
        return None

    del item.stash[_LOG_CAPTURE_KEY]
    logger.remove(capture.handler_id)
    try:
        return capture.buffer.getvalue()
    finally:
        capture.buffer.close()


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_protocol(item: Item) -> Generator[None, object, None]:
    if not item.config.getoption("allure_report_dir", default=None):
        yield
        return

    buffer = StringIO()
    capture = _LogCapture(
        buffer=buffer,
        handler_id=logger.add(
            buffer,
            level="DEBUG",
            format=_ALLURE_LOG_FORMAT,
            colorize=False,
            diagnose=False,
            enqueue=False,
        ),
    )
    item.stash[_LOG_CAPTURE_KEY] = capture

    try:
        yield
    finally:
        _stop_log_capture(item)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item) -> Generator[None, Result[TestReport], None]:
    outcome = yield
    report = outcome.get_result()
    if report.when != "teardown":
        return

    test_log = _stop_log_capture(item)
    if test_log is None:
        return

    allure.attach(
        test_log,
        name="Test log",
        attachment_type=allure.attachment_type.TEXT,
    )
