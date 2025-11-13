import reflex as rx


def delete_dialog(
    is_open: rx.Var[bool],
    on_cancel: rx.event.EventType,
    on_confirm: rx.event.EventType,
    item_type: str,
    item_name: rx.Var[str],
) -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(class_name="fixed inset-0 bg-black/30"),
            rx.radix.primitives.dialog.content(
                rx.el.h3(f"Delete {item_type}", class_name="text-lg font-semibold"),
                rx.el.p(
                    "Are you sure you want to delete ",
                    rx.el.span(item_name, class_name="font-semibold"),
                    "? This action cannot be undone.",
                    class_name="text-sm text-gray-500 mt-2",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        on_click=on_cancel,
                        class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300",
                    ),
                    rx.el.button(
                        "Delete",
                        on_click=on_confirm,
                        class_name="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600",
                    ),
                    class_name="flex justify-end gap-4 mt-6",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-lg p-6 max-w-md w-full",
            ),
        ),
        open=is_open,
    )