import reflex as rx
from app.states.student_state import StudentState


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


def student_form() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(class_name="fixed inset-0 bg-black/30"),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    rx.cond(
                        StudentState.form_mode == "add",
                        "Add New Student",
                        "Edit Student",
                    ),
                    class_name="text-lg font-semibold text-gray-800",
                ),
                rx.el.form(
                    rx.el.div(
                        _form_field(
                            "Full Name",
                            "name",
                            StudentState.form_student["name"],
                            StudentState.handle_form_change,
                            "e.g. Alice Johnson",
                        ),
                        _form_field(
                            "Email Address",
                            "email",
                            StudentState.form_student["email"],
                            StudentState.handle_form_change,
                            "e.g. alice@example.com",
                            type="email",
                        ),
                        _form_field(
                            "Phone Number",
                            "phone",
                            StudentState.form_student["phone"],
                            StudentState.handle_form_change,
                            "e.g. 123-456-7890",
                            type="tel",
                        ),
                        _form_field(
                            "Date of Birth",
                            "dob",
                            StudentState.form_student["dob"],
                            StudentState.handle_form_change,
                            "YYYY-MM-DD",
                            type="date",
                        ),
                        _form_field(
                            "Address",
                            "address",
                            StudentState.form_student["address"],
                            StudentState.handle_form_change,
                            "e.g. 123 Oak St",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Status",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.select(
                                ["Active", "Inactive"],
                                value=StudentState.form_student["status"],
                                on_change=lambda val: StudentState.handle_form_change(
                                    "status", val
                                ),
                                class_name="border-gray-200 rounded-lg text-sm w-full",
                            ),
                        ),
                        class_name="flex flex-col gap-4 mt-4",
                    ),
                    on_submit=lambda _: StudentState.save_student(),
                    prevent_default=True,
                ),
                rx.el.div(
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            "Cancel",
                            on_click=StudentState.close_form_modal,
                            class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 font-medium",
                        )
                    ),
                    rx.el.button(
                        "Save Student",
                        on_click=StudentState.save_student,
                        class_name="px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600 font-medium",
                    ),
                    class_name="flex justify-end gap-4 mt-6",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-lg p-6 max-w-lg w-full max-h-[85vh] overflow-y-auto",
            ),
        ),
        open=StudentState.is_form_modal_open,
    )