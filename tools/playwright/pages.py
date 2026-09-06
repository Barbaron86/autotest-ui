from collections.abc import Iterator

import allure
from playwright.sync_api import Page, Playwright


def initialize_playwright_page(
    playwright: Playwright, test_name: str, storage_state: str | None = None
) -> Iterator[Page]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=storage_state, record_video_dir="./videos")
    context.tracing.start(name="trace", screenshots=True, snapshots=True, sources=True, title=test_name)
    page = context.new_page()

    yield page

    video = page.video
    context.tracing.stop(path=f"./tracing/{test_name}.zip")
    context.close()
    browser.close()

    allure.attach.file(  # type: ignore[no-untyped-call]
        source=f"./tracing/{test_name}.zip",
        name=f"trace-{test_name}",
        attachment_type=allure.attachment_type.WEBM,
    )
    if video:
        allure.attach.file(
            source=video.path(),
            name=f"video-{test_name}.webm",
            attachment_type=allure.attachment_type.WEBM,
        )  # type: ignore[no-untyped-call]
