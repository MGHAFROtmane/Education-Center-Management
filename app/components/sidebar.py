import reflex as rx
from app.states.base_state import BaseState, NavItem


def nav_item(item: NavItem) -> rx.Component:
    return rx.el.a(
        rx.icon(item["icon"], class_name="h-5 w-5"),
        rx.el.span(item["name"]),
        href=item["href"],
        on_click=lambda: BaseState.set_active_page(item["name"]),
        class_name=rx.cond(
            BaseState.current_route == item["href"],
            "flex items-center gap-3 rounded-lg bg-orange-100 px-3 py-2 text-orange-600 transition-all hover:text-orange-700 font-semibold",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("book-marked", class_name="h-7 w-7 text-orange-600"),
                    rx.el.span(
                        "EduCenter",
                        class_name="text-xl font-bold tracking-tight text-gray-800",
                    ),
                    href="/",
                    class_name="flex items-center gap-2",
                ),
                class_name="flex h-16 items-center border-b px-6",
            ),
            rx.el.div(
                rx.el.nav(
                    rx.foreach(BaseState.nav_items, nav_item),
                    class_name="flex flex-col gap-1 p-4",
                ),
                class_name="flex-1 overflow-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="https://api.dicebear.com/9.x/notionists/svg?seed=Admin",
                            class_name="h-10 w-10 rounded-full",
                        ),
                        rx.el.div(
                            rx.el.p("Admin User", class_name="font-semibold text-sm"),
                            rx.el.p(
                                "admin@educenter.com",
                                class_name="text-xs text-gray-500",
                            ),
                            class_name="flex flex-col",
                        ),
                    ),
                    rx.icon(
                        "log-out",
                        class_name="h-5 w-5 text-gray-500 hover:text-orange-600 cursor-pointer",
                    ),
                    class_name="flex items-center justify-between",
                ),
                class_name="mt-auto border-t p-4",
            ),
            class_name="flex h-full max-h-screen flex-col gap-2",
        ),
        class_name="flex flex-col border-r bg-gray-50 w-64 shrink-0",
    )