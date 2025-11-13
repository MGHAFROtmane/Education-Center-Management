import reflex as rx
from app.states.dashboard_state import DashboardState

TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "border_color": "#E8E8E8",
        "border_radius": "0.75rem",
        "box_shadow": "0px 2px 6px 0px rgba(28, 32, 36, 0.02)",
        "font_family": "Open Sans, sans-serif",
        "font_size": "12px",
    },
    "cursor": {"stroke": "#f97316", "stroke_width": 2},
    "separator": ": ",
}


def enrollment_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Student Enrollment Trends",
            class_name="text-lg font-semibold text-gray-800 mb-4",
        ),
        rx.el.div(
            rx.recharts.area_chart(
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    stroke_dasharray="3 3",
                    class_name="stroke-gray-200",
                ),
                rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_line=False,
                    class_name="text-xs text-gray-500",
                ),
                rx.recharts.y_axis(
                    axis_line=False, tick_line=False, class_name="text-xs text-gray-500"
                ),
                rx.recharts.area(
                    data_key="enrollments",
                    type_="natural",
                    stroke="#f97316",
                    fill="rgba(249, 115, 22, 0.2)",
                    stroke_width=2,
                    dot=False,
                    active_dot={
                        "r": 6,
                        "stroke_width": 2,
                        "fill": "#f97316",
                        "stroke": "white",
                    },
                ),
                data=DashboardState.enrollment_trend,
                height=300,
                margin={"left": -20, "top": 10},
                class_name="[&_.recharts-tooltip-cursor]:stroke-orange-500",
            ),
            class_name="h-[300px]",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm",
    )