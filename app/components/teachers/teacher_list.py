import reflex as rx
from app.states.teacher_state import TeacherState, Teacher


def _specialization_tag(spec: str) -> rx.Component:
    colors = {
        "default": "bg-gray-100 text-gray-800",
        "python": "bg-blue-100 text-blue-800",
        "data science": "bg-indigo-100 text-indigo-800",
        "web development": "bg-purple-100 text-purple-800",
        "ui/ux design": "bg-pink-100 text-pink-800",
        "machine learning": "bg-green-100 text-green-800",
    }
    color_class = colors.get(spec.lower(), colors["default"])
    return rx.el.span(
        spec,
        class_name=f"text-xs font-medium px-2.5 py-0.5 rounded-full {color_class} w-fit",
    )


def teacher_card(teacher: Teacher) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/initials/svg?seed={teacher['name']}",
                class_name="h-16 w-16 rounded-full bg-gray-100",
            ),
            rx.el.div(
                rx.el.p(teacher["name"], class_name="font-semibold text-gray-900"),
                rx.el.p(teacher["email"], class_name="text-sm text-gray-500"),
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.p(
                "Specializations",
                class_name="text-xs font-medium text-gray-400 uppercase tracking-wider",
            ),
            rx.el.div(
                rx.foreach(teacher["specializations"], _specialization_tag),
                class_name="flex flex-wrap gap-2 mt-2",
            ),
            class_name="mt-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    teacher["assigned_courses"].length(),
                    class_name="font-semibold text-gray-900",
                ),
                rx.el.p("Assigned Courses", class_name="text-sm text-gray-500"),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.span(
                    teacher["status"],
                    class_name=rx.cond(
                        teacher["status"] == "Active",
                        "inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 w-fit",
                        "inline-flex items-center rounded-full bg-yellow-100 px-2.5 py-0.5 text-xs font-medium text-yellow-800 w-fit",
                    ),
                ),
                rx.el.p("Status", class_name="text-sm text-gray-500 mt-1"),
                class_name="text-center",
            ),
            class_name="mt-4 grid grid-cols-2 gap-4 pt-4 border-t border-gray-100",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("pencil", class_name="h-4 w-4 mr-1"),
                "Edit",
                on_click=lambda: TeacherState.open_edit_modal(teacher),
                class_name="flex-1 flex items-center justify-center p-2 text-sm text-gray-500 hover:text-green-600 hover:bg-gray-100 rounded-md transition-colors font-medium",
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="h-4 w-4 mr-1"),
                "Delete",
                on_click=lambda: TeacherState.open_delete_dialog(teacher),
                class_name="flex-1 flex items-center justify-center p-2 text-sm text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-md transition-colors font-medium",
            ),
            class_name="mt-4 flex gap-2 border-t border-gray-100 pt-4",
        ),
        class_name="bg-white p-4 rounded-xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between h-full",
    )


def teacher_list() -> rx.Component:
    return rx.el.div(
        rx.foreach(TeacherState.filtered_teachers, teacher_card),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
    )