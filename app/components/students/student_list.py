import reflex as rx
from app.states.student_state import StudentState, Student
from app.components.shared.delete_dialog import delete_dialog


def _header_cell(name: str, key: str) -> rx.Component:
    return rx.el.th(
        rx.el.div(
            name,
            rx.icon(
                tag=rx.cond(
                    StudentState.sort_order == "asc",
                    "arrow-up-narrow-wide",
                    "arrow-down-wide-narrow",
                ),
                class_name=rx.cond(
                    StudentState.sort_by == key, "opacity-100", "opacity-20"
                ),
            ),
            on_click=lambda: StudentState.set_sort(key),
            class_name="flex items-center gap-1 cursor-pointer select-none hover:text-gray-900 transition-colors",
        ),
        scope="col",
        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
    )


def _table_row(student: Student) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={student['name']}",
                    class_name="h-10 w-10 rounded-full bg-gray-100",
                ),
                rx.el.div(
                    rx.el.p(student["name"], class_name="font-medium text-gray-900"),
                    rx.el.p(student["email"], class_name="text-sm text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            student["phone"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                student["status"],
                class_name=rx.cond(
                    student["status"] == "Active",
                    "inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 w-fit",
                    "inline-flex items-center rounded-full bg-red-100 px-2.5 py-0.5 text-xs font-medium text-red-800 w-fit",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            student["enrolled_courses"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("eye", class_name="h-4 w-4"),
                    class_name="p-1 text-gray-400 hover:text-blue-600 hover:bg-gray-100 rounded-md transition-colors",
                ),
                rx.el.button(
                    rx.icon("pencil", class_name="h-4 w-4"),
                    on_click=lambda: StudentState.open_edit_modal(student),
                    class_name="p-1 text-gray-400 hover:text-green-600 hover:bg-gray-100 rounded-md transition-colors",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    on_click=lambda: StudentState.open_delete_dialog(student),
                    class_name="p-1 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-md transition-colors",
                ),
                class_name="flex items-center justify-end gap-2",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-right",
        ),
        class_name="hover:bg-gray-50/50 transition-colors",
    )


def student_table() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        _header_cell("Name", "name"),
                        _header_cell("Phone", "phone"),
                        _header_cell("Status", "status"),
                        _header_cell("Enrolled Courses", "enrolled_courses"),
                        rx.el.th(
                            rx.el.span("Actions", class_name="sr-only"),
                            scope="col",
                            class_name="relative px-6 py-3",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(StudentState.filtered_students, _table_row),
                    class_name="bg-white divide-y divide-gray-100",
                ),
                class_name="min-w-full divide-y divide-gray-200 table-auto",
            ),
            class_name="overflow-x-auto rounded-lg border border-gray-100 shadow-sm",
        ),
        delete_dialog(
            is_open=StudentState.is_delete_dialog_open,
            on_cancel=StudentState.close_delete_dialog,
            on_confirm=StudentState.delete_student,
            item_type="student",
            item_name=StudentState.student_to_delete_name,
        ),
        class_name="w-full",
    )