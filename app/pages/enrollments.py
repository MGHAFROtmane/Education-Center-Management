import reflex as rx
from app.components.layout import main_layout
from app.states.enrollment_state import EnrollmentState, EnrollmentRow
from app.states.student_state import StudentState, Student
from app.states.course_state import CourseState, Course


def enrollment_row(enrollment: EnrollmentRow) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            enrollment["student_name"],
            class_name="px-6 py-4 whitespace-nowrap font-medium text-gray-800",
        ),
        rx.el.td(
            enrollment["course_name"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            enrollment["enrollment_date"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                enrollment["status"],
                class_name=rx.match(
                    enrollment["status"],
                    (
                        "Active",
                        "inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800 w-fit",
                    ),
                    (
                        "Completed",
                        "inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 w-fit",
                    ),
                    (
                        "Dropped",
                        "inline-flex items-center rounded-full bg-red-100 px-2.5 py-0.5 text-xs font-medium text-red-800 w-fit",
                    ),
                    "",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        class_name="hover:bg-gray-50/50 transition-colors",
    )


def enrollments_page() -> rx.Component:
    return main_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Enrollments", class_name="text-3xl font-bold text-gray-800"
                    ),
                    rx.el.p(
                        "Track and manage all student enrollments.",
                        class_name="text-gray-500",
                    ),
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Student",
                                scope="col",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Course",
                                scope="col",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Enrollment Date",
                                scope="col",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
                                scope="col",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(EnrollmentState.enrollment_rows, enrollment_row),
                        class_name="bg-white divide-y divide-gray-100",
                    ),
                    class_name="min-w-full divide-y divide-gray-200 table-auto",
                ),
                class_name="overflow-x-auto rounded-lg border border-gray-100 shadow-sm",
            ),
            class_name="p-6 sm:p-8 w-full",
        )
    )