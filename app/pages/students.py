import reflex as rx
from app.components.layout import main_layout
from app.states.student_state import StudentState
from app.components.students.student_list import student_table
from app.components.students.student_form import student_form


def students_page() -> rx.Component:
    return main_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1("Students", class_name="text-3xl font-bold text-gray-800"),
                    rx.el.p(
                        "Manage all students in the center.", class_name="text-gray-500"
                    ),
                ),
                rx.el.button(
                    rx.icon("plus", class_name="mr-2 h-4 w-4"),
                    "Add Student",
                    on_click=StudentState.open_add_modal,
                    class_name="flex items-center bg-orange-500 text-white px-4 py-2 rounded-lg font-medium hover:bg-orange-600 transition-colors",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        placeholder="Search by name or email...",
                        on_change=StudentState.set_search_query,
                        default_value=StudentState.search_query,
                        class_name="w-full max-w-sm bg-white border border-gray-200 rounded-lg pl-9 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400",
                    ),
                    class_name="relative",
                ),
                rx.el.select(
                    ["All", "Active", "Inactive"],
                    value=StudentState.status_filter,
                    on_change=StudentState.set_status_filter,
                    class_name="border-gray-200 rounded-lg text-sm",
                ),
                class_name="flex items-center gap-4 mb-6",
            ),
            student_table(),
            student_form(),
            class_name="p-6 sm:p-8 w-full",
        )
    )