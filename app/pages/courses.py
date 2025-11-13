import reflex as rx
from app.components.layout import main_layout
from app.states.course_state import CourseState
from app.states.teacher_state import TeacherState
from app.components.shared.delete_dialog import delete_dialog


def _grid_view_toggle() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("layout-grid", class_name="h-4 w-4"),
            on_click=lambda: CourseState.set_view_mode("grid"),
            class_name=rx.cond(
                CourseState.view_mode == "grid",
                "p-2 bg-orange-100 text-orange-600 rounded-md",
                "p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-md",
            ),
        ),
        rx.el.button(
            rx.icon("list", class_name="h-4 w-4"),
            on_click=lambda: CourseState.set_view_mode("list"),
            class_name=rx.cond(
                CourseState.view_mode == "list",
                "p-2 bg-orange-100 text-orange-600 rounded-md",
                "p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-md",
            ),
        ),
        class_name="flex items-center bg-gray-50 border border-gray-200 rounded-lg p-1",
    )


def _course_card(course: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                course["category"],
                class_name="text-xs font-semibold text-orange-600 bg-orange-100 px-2 py-1 rounded-full w-fit",
            ),
            rx.el.p(
                course["status"],
                class_name=rx.cond(
                    course["status"] == "Published",
                    "text-xs font-semibold text-green-600 bg-green-100 px-2 py-1 rounded-full w-fit",
                    "text-xs font-semibold text-gray-600 bg-gray-100 px-2 py-1 rounded-full w-fit",
                ),
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.h3(
            course["title"],
            class_name="font-semibold text-lg text-gray-800 mt-3 truncate",
        ),
        rx.el.p(
            course["description"],
            class_name="text-sm text-gray-500 mt-1 h-10 overflow-hidden text-ellipsis",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("users", class_name="h-4 w-4 text-gray-400"),
                rx.el.p(
                    f"{course['enrolled_students']} / {course['capacity']} students",
                    class_name="text-sm text-gray-600",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.icon("clock", class_name="h-4 w-4 text-gray-400"),
                rx.el.p(
                    f"{course['duration_hours']} hours",
                    class_name="text-sm text-gray-600",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between text-sm mt-4 pt-4 border-t border-gray-100",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("pencil", class_name="h-4 w-4 mr-1"),
                "Edit",
                on_click=lambda: CourseState.open_edit_modal(course),
                class_name="flex-1 flex items-center justify-center p-2 text-sm text-gray-500 hover:text-green-600 hover:bg-gray-100 rounded-md transition-colors font-medium",
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="h-4 w-4 mr-1"),
                "Delete",
                on_click=lambda: CourseState.open_delete_dialog(course),
                class_name="flex-1 flex items-center justify-center p-2 text-sm text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-md transition-colors font-medium",
            ),
            class_name="mt-4 flex gap-2 border-t border-gray-100 pt-3",
        ),
        class_name="bg-white p-4 rounded-xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between h-full",
    )


def _course_list_item(course: rx.Var[dict]) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            course["title"],
            class_name="px-6 py-4 whitespace-nowrap font-medium text-gray-800",
        ),
        rx.el.td(
            course["category"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            f"{course['duration_hours']}h",
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            f"{course['enrolled_students']} / {course['capacity']}",
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                course["status"],
                class_name=rx.cond(
                    course["status"] == "Published",
                    "inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 w-fit",
                    "inline-flex items-center rounded-full bg-gray-100 px-2.5 py-0.5 text-xs font-medium text-gray-800 w-fit",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("pencil", class_name="h-4 w-4"),
                    on_click=lambda: CourseState.open_edit_modal(course),
                    class_name="p-1 text-gray-400 hover:text-green-600 hover:bg-gray-100 rounded-md transition-colors",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    on_click=lambda: CourseState.open_delete_dialog(course),
                    class_name="p-1 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-md transition-colors",
                ),
                class_name="flex items-center justify-end gap-2",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-right",
        ),
        class_name="hover:bg-gray-50/50 transition-colors",
    )


def _form_field(
    label, name, value, on_change, placeholder, type="text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            name=name,
            type=type,
            default_value=value,
            on_change=lambda val: on_change(name, val),
            placeholder=placeholder,
            class_name="w-full bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400",
        ),
        class_name="w-full",
    )


def course_form() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(class_name="fixed inset-0 bg-black/30"),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    rx.cond(
                        CourseState.form_mode == "add", "Add New Course", "Edit Course"
                    ),
                    class_name="text-lg font-semibold text-gray-800",
                ),
                rx.el.form(
                    rx.el.div(
                        _form_field(
                            "Course Title",
                            "title",
                            CourseState.form_course["title"],
                            CourseState.handle_form_change,
                            "e.g. Intro to Reflex",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Description",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.textarea(
                                name="description",
                                default_value=CourseState.form_course["description"],
                                on_change=lambda val: CourseState.handle_form_change(
                                    "description", val
                                ),
                                placeholder="A short description of the course...",
                                class_name="w-full bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400 h-24",
                            ),
                        ),
                        rx.el.div(
                            _form_field(
                                "Category",
                                "category",
                                CourseState.form_course["category"],
                                CourseState.handle_form_change,
                                "e.g. Programming",
                            ),
                            _form_field(
                                "Duration (hours)",
                                "duration_hours",
                                CourseState.form_course["duration_hours"].to_string(),
                                CourseState.handle_form_change,
                                "e.g. 40",
                                type="number",
                            ),
                            class_name="grid grid-cols-2 gap-4",
                        ),
                        rx.el.div(
                            _form_field(
                                "Capacity",
                                "capacity",
                                CourseState.form_course["capacity"].to_string(),
                                CourseState.handle_form_change,
                                "e.g. 25",
                                type="number",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Instructor",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("Select an instructor", value=""),
                                    rx.foreach(
                                        TeacherState.teachers,
                                        lambda t: rx.el.option(
                                            t["name"], value=t["id"].to_string()
                                        ),
                                    ),
                                    value=CourseState.form_course[
                                        "instructor_id"
                                    ].to_string(),
                                    on_change=lambda val: CourseState.handle_form_change(
                                        "instructor_id", val
                                    ),
                                    class_name="border-gray-200 rounded-lg text-sm w-full",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Status",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.select(
                                ["Published", "Draft"],
                                value=CourseState.form_course["status"],
                                on_change=lambda val: CourseState.handle_form_change(
                                    "status", val
                                ),
                                class_name="border-gray-200 rounded-lg text-sm w-full",
                            ),
                        ),
                        class_name="flex flex-col gap-4 mt-4",
                    ),
                    on_submit=lambda _: CourseState.save_course(),
                    prevent_default=True,
                ),
                rx.el.div(
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            "Cancel",
                            on_click=CourseState.close_form_modal,
                            class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 font-medium",
                        )
                    ),
                    rx.el.button(
                        "Save Course",
                        on_click=CourseState.save_course,
                        class_name="px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600 font-medium",
                    ),
                    class_name="flex justify-end gap-4 mt-6",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-lg p-6 max-w-lg w-full max-h-[85vh] overflow-y-auto",
            ),
        ),
        open=CourseState.is_form_modal_open,
    )


def courses_page() -> rx.Component:
    return main_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1("Courses", class_name="text-3xl font-bold text-gray-800"),
                    rx.el.p(
                        "Manage all courses offered in the center.",
                        class_name="text-gray-500",
                    ),
                ),
                rx.el.button(
                    rx.icon("plus", class_name="mr-2 h-4 w-4"),
                    "Add Course",
                    on_click=CourseState.open_add_modal,
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
                        placeholder="Search by course title...",
                        on_change=CourseState.set_search_query,
                        default_value=CourseState.search_query,
                        class_name="w-full max-w-sm bg-white border border-gray-200 rounded-lg pl-9 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400",
                    ),
                    class_name="relative",
                ),
                rx.el.div(
                    rx.el.select(
                        rx.el.option("All Categories", value="All"),
                        rx.foreach(
                            CourseState.course_categories,
                            lambda cat: rx.el.option(cat, value=cat),
                        ),
                        value=CourseState.category_filter,
                        on_change=CourseState.set_category_filter,
                        class_name="border-gray-200 rounded-lg text-sm",
                    ),
                    _grid_view_toggle(),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.cond(
                CourseState.view_mode == "grid",
                rx.el.div(
                    rx.foreach(CourseState.filtered_courses, _course_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Title",
                                    scope="col",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Category",
                                    scope="col",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Duration",
                                    scope="col",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Enrollment",
                                    scope="col",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Status",
                                    scope="col",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    rx.el.span("Actions", class_name="sr-only"),
                                    scope="col",
                                    class_name="relative px-6 py-3",
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(CourseState.filtered_courses, _course_list_item),
                            class_name="bg-white divide-y divide-gray-100",
                        ),
                        class_name="min-w-full divide-y divide-gray-200 table-auto",
                    ),
                    class_name="overflow-x-auto rounded-lg border border-gray-100 shadow-sm",
                ),
            ),
            course_form(),
            delete_dialog(
                is_open=CourseState.is_delete_dialog_open,
                on_cancel=CourseState.close_delete_dialog,
                on_confirm=CourseState.delete_course,
                item_type="course",
                item_name=CourseState.course_to_delete_title,
            ),
            class_name="p-6 sm:p-8 w-full",
        )
    )