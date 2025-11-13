import reflex as rx
from app.components.sidebar import sidebar


def main_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(child, class_name="flex-1 overflow-y-auto w-full"),
        class_name="flex min-h-screen w-full bg-gray-50/50",
    )