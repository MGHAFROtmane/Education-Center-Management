import reflex as rx
from app.components.layout import main_layout
from app.states.teacher_state import TeacherState
from app.components.teachers.teacher_list import teacher_list
from app.components.teachers.teacher_form import teacher_form
from app.components.shared.delete_dialog import delete_dialog


def teachers_page() -> rx.Component:
    return main_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1("Teachers", class_name="text-3xl font-bold text-gray-800"),
                    rx.el.p(
                        "Manage all teachers in the center.", class_name="text-gray-500"
                    ),
                ),
                rx.el.button(
                    rx.icon("plus", class_name="mr-2 h-4 w-4"),
                    "Add Teacher",
                    on_click=TeacherState.open_add_modal,
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
                        on_change=TeacherState.set_search_query,
                        default_value=TeacherState.search_query,
                        class_name="w-full max-w-sm bg-white border border-gray-200 rounded-lg pl-9 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400",
                    ),
                    class_name="relative",
                ),
                class_name="flex items-center gap-4 mb-6",
            ),
            teacher_list(),
            teacher_form(),
            delete_dialog(
                is_open=TeacherState.is_delete_dialog_open,
                on_cancel=TeacherState.close_delete_dialog,
                on_confirm=TeacherState.delete_teacher,
                item_type="teacher",
                item_name=TeacherState.teacher_to_delete_name,
            ),
            class_name="p-6 sm:p-8 w-full",
        )
    )