import reflex as rx
from typing import TypedDict, Literal, Optional
import random


class Teacher(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    specializations: list[str]
    bio: str
    assigned_courses: list[int]
    status: Literal["Active", "On Leave"]


SAMPLE_TEACHERS: list[Teacher] = [
    {
        "id": 1,
        "name": "Dr. Evelyn Reed",
        "email": "e.reed@educenter.com",
        "phone": "111-222-3333",
        "specializations": ["Data Science", "Machine Learning"],
        "bio": "PhD in Computer Science with a focus on AI. 10+ years of teaching experience.",
        "assigned_courses": [3, 4],
        "status": "Active",
    },
    {
        "id": 2,
        "name": "Mr. Samuel Chen",
        "email": "s.chen@educenter.com",
        "phone": "222-333-4444",
        "specializations": ["Web Development", "JavaScript"],
        "bio": "Full-stack developer with a passion for teaching modern web technologies.",
        "assigned_courses": [2],
        "status": "Active",
    },
    {
        "id": 3,
        "name": "Ms. Anita Desai",
        "email": "a.desai@educenter.com",
        "phone": "333-444-5555",
        "specializations": ["Python", "Beginner Courses"],
        "bio": "Loves introducing new students to the world of programming.",
        "assigned_courses": [1],
        "status": "Active",
    },
    {
        "id": 4,
        "name": "Mr. Ben Carter",
        "email": "b.carter@educenter.com",
        "phone": "444-555-6666",
        "specializations": ["UI/UX Design"],
        "bio": "Award-winning designer focused on user-centric design principles.",
        "assigned_courses": [5],
        "status": "On Leave",
    },
    {
        "id": 5,
        "name": "Dr. Maria Garcia",
        "email": "m.garcia@educenter.com",
        "phone": "555-666-7777",
        "specializations": ["Cybersecurity", "Networking"],
        "bio": "Cybersecurity expert with real-world experience in threat analysis.",
        "assigned_courses": [],
        "status": "Active",
    },
    {
        "id": 6,
        "name": "Mr. Kenji Tanaka",
        "email": "k.tanaka@educenter.com",
        "phone": "666-777-8888",
        "specializations": ["Mobile Development", "React Native"],
        "bio": "Passionate about creating beautiful and functional mobile applications.",
        "assigned_courses": [],
        "status": "Active",
    },
    {
        "id": 7,
        "name": "Ms. Olivia White",
        "email": "o.white@educenter.com",
        "phone": "777-888-9999",
        "specializations": ["Project Management", "Agile"],
        "bio": "Certified Scrum Master and project management professional.",
        "assigned_courses": [],
        "status": "Active",
    },
    {
        "id": 8,
        "name": "Mr. David Lee",
        "email": "d.lee@educenter.com",
        "phone": "888-999-0000",
        "specializations": ["Cloud Computing", "AWS"],
        "bio": "AWS Certified Solutions Architect with extensive industry experience.",
        "assigned_courses": [],
        "status": "Active",
    },
]


class TeacherState(rx.State):
    teachers: list[Teacher] = SAMPLE_TEACHERS
    search_query: str = ""
    is_delete_dialog_open: bool = False
    teacher_to_delete: Optional[Teacher] = None
    is_form_modal_open: bool = False
    form_mode: Literal["add", "edit"] = "add"
    form_teacher: Teacher = {
        "id": 0,
        "name": "",
        "email": "",
        "phone": "",
        "specializations": [],
        "bio": "",
        "assigned_courses": [],
        "status": "Active",
    }
    form_specializations_str: str = ""

    @rx.var
    def filtered_teachers(self) -> list[Teacher]:
        if self.search_query:
            return [
                t
                for t in self.teachers
                if self.search_query.lower() in t["name"].lower()
                or self.search_query.lower() in t["email"].lower()
            ]
        return self.teachers

    @rx.event
    def open_delete_dialog(self, teacher: Teacher):
        self.is_delete_dialog_open = True
        self.teacher_to_delete = teacher

    @rx.event
    def close_delete_dialog(self):
        self.is_delete_dialog_open = False
        self.teacher_to_delete = None

    @rx.event
    def delete_teacher(self):
        if self.teacher_to_delete:
            self.teachers = [
                t for t in self.teachers if t["id"] != self.teacher_to_delete["id"]
            ]
            self.close_delete_dialog()
            return rx.toast.success(
                f"Teacher '{self.teacher_to_delete['name']}' deleted."
            )

    @rx.var
    def teacher_to_delete_name(self) -> str:
        return self.teacher_to_delete["name"] if self.teacher_to_delete else ""

    @rx.event
    def open_add_modal(self):
        self.form_mode = "add"
        self.form_teacher = {
            "id": 0,
            "name": "",
            "email": "",
            "phone": "",
            "specializations": [],
            "bio": "",
            "assigned_courses": [],
            "status": "Active",
        }
        self.form_specializations_str = ""
        self.is_form_modal_open = True

    @rx.event
    def open_edit_modal(self, teacher: Teacher):
        self.form_mode = "edit"
        self.form_teacher = teacher
        self.form_specializations_str = ", ".join(teacher["specializations"])
        self.is_form_modal_open = True

    @rx.event
    def close_form_modal(self):
        self.is_form_modal_open = False

    def _set_form_teacher_field(self, key: str, value: str):
        self.form_teacher[key] = value

    @rx.event
    def handle_form_change(self, field: str, value: str):
        if field == "specializations":
            self.form_specializations_str = value
            self.form_teacher["specializations"] = [
                s.strip() for s in value.split(",") if s.strip()
            ]
        else:
            self._set_form_teacher_field(field, value)

    @rx.event
    def save_teacher(self):
        if not self.form_teacher["name"] or not self.form_teacher["email"]:
            return rx.toast.error("Name and email are required.")
        if self.form_mode == "add":
            new_teacher = self.form_teacher.copy()
            new_teacher["id"] = (
                max((t["id"] for t in self.teachers)) + 1 if self.teachers else 1
            )
            self.teachers.append(new_teacher)
            yield rx.toast.success(f"Teacher '{new_teacher['name']}' added.")
        else:
            self.teachers = [
                self.form_teacher if t["id"] == self.form_teacher["id"] else t
                for t in self.teachers
            ]
            yield rx.toast.success(f"Teacher '{self.form_teacher['name']}' updated.")
        self.close_form_modal()