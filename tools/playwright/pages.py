from collections.abc import Iterator
from pathlib import Path

import allure
from playwright.sync_api import Page, Playwright

from config import settings


def initialize_playwright_page(
    playwright: Playwright, test_name: str, storage_state: Path | None = None
) -> Iterator[Page]:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(storage_state=storage_state, record_video_dir=settings.videos_dir)
    context.tracing.start(name="trace", screenshots=True, snapshots=True, sources=True, title=test_name)
    page = context.new_page()

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
