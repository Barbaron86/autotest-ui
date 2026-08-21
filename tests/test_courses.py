from playwright.sync_api import expect, sync_playwright


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("emailtest@gmail.com")

        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username")

        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        context.storage_state(path="browser_state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser_state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_toolbar_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_list_toolbar_title).to_have_text("Courses")

        courses_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_icon).to_be_visible()

        courses_list_empty_view_title = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_list_empty_view_title).to_have_text("There is no results")

        courses_list_empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_list_empty_view_description).to_have_text(
            "Results from the load test pipeline will be displayed here"
        )
