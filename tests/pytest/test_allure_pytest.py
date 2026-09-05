import allure


@allure.step("Open browser")
def open_browser():
    with allure.step("Get browser"):
        ...

    with allure.step("Start browser"):
        with allure.step("Loading browser"):
            ...


@allure.step("Create course with title: {title}")
def create_course(title: str): ...


@allure.step("Close browser")
def close_browser(): ...


def test_feature():
    with allure.step("Step 1"):
        ...
    with allure.step("Step 2"):
        ...
    with allure.step("Step 3"):
        ...


def test_allure_steps():
    open_browser()
    create_course(title="Playwright")
    close_browser()
