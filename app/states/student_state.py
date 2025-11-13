import reflex as rx
import datetime
from typing import TypedDict, Literal, Optional


class Student(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    status: Literal["Active", "Inactive"]
    enrolled_courses: int
    dob: str
    address: str


SAMPLE_STUDENTS: list[Student] = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "phone": "123-456-7890",
        "status": "Active",
        "enrolled_courses": 3,
        "dob": "1998-05-12",
        "address": "123 Oak St",
    },
    {
        "id": 2,
        "name": "Bob Williams",
        "email": "bob@example.com",
        "phone": "234-567-8901",
        "status": "Active",
        "enrolled_courses": 2,
        "dob": "1999-02-20",
        "address": "456 Pine St",
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "email": "charlie@example.com",
        "phone": "345-678-9012",
        "status": "Inactive",
        "enrolled_courses": 1,
        "dob": "1997-11-30",
        "address": "789 Maple Ave",
    },
    {
        "id": 4,
        "name": "Diana Miller",
        "email": "diana@example.com",
        "phone": "456-789-0123",
        "status": "Active",
        "enrolled_courses": 4,
        "dob": "2000-07-22",
        "address": "101 Birch Rd",
    },
    {
        "id": 5,
        "name": "Ethan Davis",
        "email": "ethan@example.com",
        "phone": "567-890-1234",
        "status": "Active",
        "enrolled_courses": 2,
        "dob": "1998-09-05",
        "address": "212 Cedar Ln",
    },
    {
        "id": 6,
        "name": "Fiona Garcia",
        "email": "fiona@example.com",
        "phone": "678-901-2345",
        "status": "Inactive",
        "enrolled_courses": 0,
        "dob": "2001-03-15",
        "address": "333 Elm Ct",
    },
    {
        "id": 7,
        "name": "George Rodriguez",
        "email": "george@example.com",
        "phone": "789-012-3456",
        "status": "Active",
        "enrolled_courses": 5,
        "dob": "1999-12-01",
        "address": "444 Spruce Way",
    },
    {
        "id": 8,
        "name": "Hannah Martinez",
        "email": "hannah@example.com",
        "phone": "890-123-4567",
        "status": "Active",
        "enrolled_courses": 3,
        "dob": "2000-08-18",
        "address": "555 Walnut Blvd",
    },
    {
        "id": 9,
        "name": "Ian Hernandez",
        "email": "ian@example.com",
        "phone": "901-234-5678",
        "status": "Active",
        "enrolled_courses": 2,
        "dob": "1997-06-10",
        "address": "666 Ash Dr",
    },
    {
        "id": 10,
        "name": "Julia Lopez",
        "email": "julia@example.com",
        "phone": "012-345-6789",
        "status": "Inactive",
        "enrolled_courses": 1,
        "dob": "2002-01-25",
        "address": "777 Willow Pass",
    },
]


class StudentState(rx.State):
    students: list[Student] = SAMPLE_STUDENTS
    search_query: str = ""
    status_filter: str = "All"
    sort_by: str = "name"
    sort_order: Literal["asc", "desc"] = "asc"
    is_delete_dialog_open: bool = False
    student_to_delete: Optional[Student] = None
    is_form_modal_open: bool = False
    form_mode: Literal["add", "edit"] = "add"
    form_student: Student = {
        "id": 0,
        "name": "",
        "email": "",
        "phone": "",
        "status": "Active",
        "enrolled_courses": 0,
        "dob": "",
        "address": "",
    }

    @rx.var
    def filtered_students(self) -> list[Student]:
        students_list = self.students
        if self.search_query:
            students_list = [
                s
                for s in students_list
                if self.search_query.lower() in s["name"].lower()
                or self.search_query.lower() in s["email"].lower()
            ]
        if self.status_filter != "All":
            students_list = [
                s for s in students_list if s["status"] == self.status_filter
            ]
        students_list.sort(
            key=lambda s: s[self.sort_by.lower().replace(" ", "_")].lower()
            if isinstance(s[self.sort_by.lower().replace(" ", "_")], str)
            else s[self.sort_by.lower().replace(" ", "_")],
            reverse=self.sort_order == "desc",
        )
        return students_list

    @rx.event
    def set_sort(self, column: str):
        if self.sort_by == column:
            self.sort_order = "desc" if self.sort_order == "asc" else "asc"
        else:
            self.sort_by = column
            self.sort_order = "asc"

    @rx.event
    def open_delete_dialog(self, student: Student):
        self.is_delete_dialog_open = True
        self.student_to_delete = student

    @rx.event
    def close_delete_dialog(self):
        self.is_delete_dialog_open = False
        self.student_to_delete = None

    @rx.event
    def delete_student(self):
        if self.student_to_delete:
            student_name = self.student_to_delete["name"]
            self.students = [
                s for s in self.students if s["id"] != self.student_to_delete["id"]
            ]
            self.close_delete_dialog()
            return rx.toast.success(f"Student '{student_name}' deleted.")

    @rx.var
    def student_to_delete_name(self) -> str:
        return self.student_to_delete["name"] if self.student_to_delete else ""

    @rx.event
    def open_add_modal(self):
        self.form_mode = "add"
        self.form_student = {
            "id": 0,
            "name": "",
            "email": "",
            "phone": "",
            "status": "Active",
            "enrolled_courses": 0,
            "dob": "",
            "address": "",
        }
        self.is_form_modal_open = True

    @rx.event
    def open_edit_modal(self, student: Student):
        self.form_mode = "edit"
        self.form_student = student
        self.is_form_modal_open = True

    @rx.event
    def close_form_modal(self):
        self.is_form_modal_open = False

    def _set_form_student_field(self, key: str, value):
        self.form_student[key] = value

    @rx.event
    def handle_form_change(self, field: str, value: str):
        self._set_form_student_field(field, value)

    @rx.event
    def save_student(self):
        if not self.form_student["name"] or not self.form_student["email"]:
            return rx.toast.error("Name and email are required.")
        if self.form_mode == "add":
            new_student = self.form_student.copy()
            new_student["id"] = (
                max((s["id"] for s in self.students)) + 1 if self.students else 1
            )
            self.students.append(new_student)
            yield rx.toast.success(f"Student '{new_student['name']}' added.")
        else:
            self.students = [
                self.form_student if s["id"] == self.form_student["id"] else s
                for s in self.students
            ]
            yield rx.toast.success(f"Student '{self.form_student['name']}' updated.")
        self.close_form_modal()