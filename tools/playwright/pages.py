from collections.abc import Iterator
from pathlib import Path

import allure
from playwright.sync_api import Page, Playwright

from config import Browser, settings
from tools.playwright.mocks import mock_static_resources


def initialize_playwright_page(
    playwright: Playwright, test_name: str, browser_type: Browser, storage_state: Path | None = None
) -> Iterator[Page]:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(), storage_state=storage_state, record_video_dir=settings.videos_dir
    )
    context.tracing.start(name="trace", screenshots=True, snapshots=True, sources=True, title=test_name)
    page = context.new_page()
    mock_static_resources(page)

    yield page

    video = page.video
    context.tracing.stop(path=settings.tracing_dir.joinpath(f"{test_name}.zip"))
    context.close()
    browser.close()

    allure.attach.file(  # type: ignore[no-untyped-call]
        source=settings.tracing_dir.joinpath(f"{test_name}.zip"),
        name=f"trace-{test_name}",
        attachment_type=allure.attachment_type.ZIP,
    )
    if video:
        allure.attach.file(
            source=video.path(),
            name=f"video-{test_name}.webm",
            attachment_type=allure.attachment_type.WEBM,
        )  # type: ignore[no-untyped-call]
