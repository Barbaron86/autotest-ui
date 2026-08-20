from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login", wait_until="networkidle"
    )

    new_text = "Authentication UI Course"
    page.evaluate(
        """
        (text) => {
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = text;
        }
        """,
        new_text,
    )
    title = page.get_by_test_id("authentication-ui-course-title-text")

    page.wait_for_timeout(5000)
