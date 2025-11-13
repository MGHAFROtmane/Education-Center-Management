import reflex as rx
from app.states.dashboard_state import DashboardState


def quick_action_button(icon: str, text: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, class_name="h-4 w-4 mr-2"),
        text,
        on_click=lambda: DashboardState.quick_action(text),
        class_name="flex items-center justify-center w-full bg-orange-500 text-white px-4 py-2 rounded-lg font-medium hover:bg-orange-600 transition-colors",
    )


def quick_actions() -> rx.Component:
    return rx.el.div(
        quick_action_button("user-plus", "Add Student"),
        quick_action_button("book-plus", "Add Course"),
        quick_action_button("clipboard-plus", "New Enrollment"),
        class_name="grid grid-cols-1 sm:grid-cols-3 gap-4",
    )