import reflex as rx
from typing import TypedDict


class NavItem(TypedDict):
    name: str
    icon: str
    href: str


class BaseState(rx.State):
    """The base state for the app, handling navigation."""

    nav_items: list[NavItem] = [
        {"name": "Dashboard", "icon": "layout-dashboard", "href": "/dashboard"},
        {"name": "Students", "icon": "users", "href": "/students"},
        {"name": "Teachers", "icon": "graduation-cap", "href": "/teachers"},
        {"name": "Courses", "icon": "book-open", "href": "/courses"},
        {"name": "Enrollments", "icon": "clipboard-list", "href": "/enrollments"},
    ]
    active_page: str = "Dashboard"

    @rx.var
    def current_route(self) -> str:
        return self.router.page.path

    @rx.event
    def set_active_page(self, page_name: str):
        self.active_page = page_name