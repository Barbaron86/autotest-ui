from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.dashboard_title = self.page.get_by_test_id("dashboard-toolbar-title-text")

        self.students_widget_title = self.page.get_by_test_id("students-widget-title-text")
        self.students_chart = self.page.get_by_test_id("students-bar-chart")

        self.activities_widget_title = self.page.get_by_test_id("activities-widget-title-text")
        self.activities_chart = self.page.get_by_test_id("activities-line-chart")

        self.courses_widget_title = self.page.get_by_test_id("courses-widget-title-text")
        self.courses_chart = self.page.get_by_test_id("courses-pie-chart")

        self.scores_widget_title = self.page.get_by_test_id("scores-widget-title-text")
        self.scores_chart = self.page.get_by_test_id("scores-scatter-chart")

    def check_visible_dashboard_title(self) -> None:
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text("Dashboard")

    def check_visible_students_widget(self) -> None:
        expect(self.students_widget_title).to_be_visible()
        expect(self.students_widget_title).to_have_text("Students")
        expect(self.students_chart).to_be_visible()

    def check_visible_activities_widget(self) -> None:
        expect(self.activities_widget_title).to_be_visible()
        expect(self.activities_widget_title).to_have_text("Activities")
        expect(self.activities_chart).to_be_visible()

    def check_visible_courses_widget(self) -> None:
        expect(self.courses_widget_title).to_be_visible()
        expect(self.courses_widget_title).to_have_text("Courses")
        expect(self.courses_chart).to_be_visible()

    def check_visible_scores_widget(self) -> None:
        expect(self.scores_widget_title).to_be_visible()
        expect(self.scores_widget_title).to_have_text("Scores")
        expect(self.scores_chart).to_be_visible()
