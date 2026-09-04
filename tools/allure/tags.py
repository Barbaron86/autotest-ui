from enum import StrEnum


class AllureTag(StrEnum):
    """
    Allure tags for test cases.
    """

    COURSES = "COURSES"
    DASHBOARD = "DASHBOARD"
    SMOKE = "SMOKE"
    REGRESSION = "REGRESSION"
    REGISTRATION = "REGISTRATION"
    NAVIGATION = "NAVIGATION"
    AUTHORIZATION = "AUTHORIZATION"
    USER_LOGIN = "USER_LOGIN"
