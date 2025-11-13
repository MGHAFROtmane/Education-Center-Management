import reflex as rx
from app.components.layout import main_layout
from app.states.dashboard_state import DashboardState
from app.components.dashboard.metric_card import metric_card
from app.components.dashboard.enrollment_chart import enrollment_chart
from app.components.dashboard.course_chart import course_chart
from app.components.dashboard.activity_feed import activity_feed
from app.components.dashboard.quick_actions import quick_actions


def dashboard() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.h1("Dashboard", class_name="text-3xl font-bold text-gray-800"),
            rx.el.p(
                "Welcome back, Admin! Here's your center's overview.",
                class_name="text-gray-500",
            ),
            class_name="mb-6",
        ),
        rx.el.div(quick_actions(), class_name="mb-6"),
        rx.el.div(
            metric_card("users", "Total Students", DashboardState.total_students),
            metric_card("book-open", "Active Courses", DashboardState.active_courses),
            metric_card(
                "graduation-cap", "Total Teachers", DashboardState.total_teachers
            ),
            metric_card(
                "line-chart", "Enrollment Rate", f"{DashboardState.enrollment_rate}%"
            ),
            class_name="grid gap-6 md:grid-cols-2 lg:grid-cols-4 mb-6",
        ),
        rx.el.div(
            enrollment_chart(),
            activity_feed(),
            class_name="grid gap-6 lg:grid-cols-3 mb-6",
        ),
        rx.el.div(course_chart(), class_name="grid gap-6"),
        class_name="p-6 sm:p-8",
    )


from app.pages.students import students_page
from app.pages.teachers import teachers_page
from app.pages.courses import courses_page
from app.pages.enrollments import enrollments_page


def index() -> rx.Component:
    return main_layout(dashboard())


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(index, route="/dashboard")
app.add_page(students_page, route="/students")
app.add_page(teachers_page, route="/teachers")
app.add_page(courses_page, route="/courses")
app.add_page(enrollments_page, route="/enrollments")