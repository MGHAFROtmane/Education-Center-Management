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
    "cursor": {"fill": "#fde68a"},
    "separator": ": ",
}


def course_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Course Popularity", class_name="text-lg font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    stroke_dasharray="3 3",
                    class_name="stroke-gray-200",
                ),
                rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                rx.recharts.x_axis(type_="number", hide=True),
                rx.recharts.y_axis(
                    data_key="name",
                    type_="category",
                    axis_line=False,
                    tick_line=False,
                    width=100,
                    class_name="text-xs text-gray-500",
                ),
                rx.recharts.bar(
                    data_key="students",
                    fill="#fb923c",
                    radius=[4, 4, 0, 0],
                    bar_size=20,
                ),
                data=DashboardState.course_popularity,
                height=300,
                layout="vertical",
                margin={"top": 10, "right": 20, "bottom": 10, "left": 10},
                class_name="[&_.recharts-label]:fill-gray-500 [&_.recharts-label]:text-xs",
            ),
            class_name="h-[300px]",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm",
    )