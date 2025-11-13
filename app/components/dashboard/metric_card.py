import reflex as rx


def metric_card(
    icon: str, title: str, value: rx.Var, rate: rx.Var | None = None
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(title, class_name="text-sm font-medium text-gray-500"),
            rx.icon(icon, class_name="h-4 w-4 text-gray-400"),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.p(value, class_name="text-2xl font-bold text-gray-800"),
            rx.cond(
                rate,
                rx.el.p(f"+{rate}%", class_name="text-xs text-green-500"),
                rx.el.div(),
            ),
            class_name="flex items-baseline gap-2",
        ),
        class_name="bg-gray-50 p-4 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow",
    )