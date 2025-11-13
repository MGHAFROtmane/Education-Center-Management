import reflex as rx
from app.states.dashboard_state import DashboardState, Activity


def activity_item(activity: Activity) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(activity["icon"], class_name="h-5 w-5 text-gray-500"),
            class_name="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100",
        ),
        rx.el.div(
            rx.el.p(activity["description"], class_name="text-sm text-gray-800"),
            rx.el.p(activity["timestamp"], class_name="text-xs text-gray-500"),
            class_name="flex-1",
        ),
        class_name="flex items-center gap-4",
    )


def activity_feed() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Recent Activity", class_name="text-lg font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.foreach(DashboardState.recent_activities, activity_item),
            class_name="flex flex-col gap-4",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm h-full",
    )