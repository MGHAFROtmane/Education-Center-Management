import reflex as rx
from app.states.teacher_state import TeacherState, Teacher


def _form_field(
    label: str,
    name: str,
    value: rx.Var,
    on_change: rx.event.EventHandler,
    placeholder: str,
    type: str = "text",
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


def _textarea_field(
    label: str,
    name: str,
    value: rx.Var,
    on_change: rx.event.EventHandler,
    placeholder: str,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.textarea(
            name=name,
            default_value=value,
            on_change=lambda val: on_change(name, val),
            placeholder=placeholder,
            class_name="w-full bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400 h-24",
        ),
        class_name="w-full",
    )


def teacher_form() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(class_name="fixed inset-0 bg-black/30"),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    rx.cond(
                        TeacherState.form_mode == "add",
                        "Add New Teacher",
                        "Edit Teacher",
                    ),
                    class_name="text-lg font-semibold text-gray-800",
                ),
                rx.el.form(
                    rx.el.div(
                        _form_field(
                            "Full Name",
                            "name",
                            TeacherState.form_teacher["name"],
                            TeacherState.handle_form_change,
                            "e.g. John Doe",
                        ),
                        _form_field(
                            "Email Address",
                            "email",
                            TeacherState.form_teacher["email"],
                            TeacherState.handle_form_change,
                            "e.g. john.doe@example.com",
                            type="email",
                        ),
                        _form_field(
                            "Phone Number",
                            "phone",
                            TeacherState.form_teacher["phone"],
                            TeacherState.handle_form_change,
                            "e.g. 123-456-7890",
                            type="tel",
                        ),
                        _form_field(
                            "Specializations (comma-separated)",
                            "specializations",
                            TeacherState.form_specializations_str,
                            TeacherState.handle_form_change,
                            "e.g. Python, Data Science",
                        ),
                        _textarea_field(
                            "Biography",
                            "bio",
                            TeacherState.form_teacher["bio"],
                            TeacherState.handle_form_change,
                            "A short bio about the teacher...",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Status",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.select(
                                ["Active", "On Leave"],
                                value=TeacherState.form_teacher["status"],
                                on_change=lambda val: TeacherState.handle_form_change(
                                    "status", val
                                ),
                                class_name="border-gray-200 rounded-lg text-sm w-full",
                            ),
                        ),
                        class_name="flex flex-col gap-4 mt-4",
                    ),
                    on_submit=lambda _: TeacherState.save_teacher(),
                    prevent_default=True,
                ),
                rx.el.div(
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            "Cancel",
                            on_click=TeacherState.close_form_modal,
                            class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 font-medium",
                        )
                    ),
                    rx.el.button(
                        "Save Teacher",
                        on_click=TeacherState.save_teacher,
                        class_name="px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600 font-medium",
                    ),
                    class_name="flex justify-end gap-4 mt-6",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-lg p-6 max-w-lg w-full max-h-[85vh] overflow-y-auto",
            ),
        ),
        open=TeacherState.is_form_modal_open,
    )