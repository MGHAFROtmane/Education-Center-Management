import reflex as rx
from typing import TypedDict, Literal, Optional


class Course(TypedDict):
    id: int
    title: str
    description: str
    category: str
    duration_hours: int
    capacity: int
    enrolled_students: int
    instructor_id: Optional[int]
    status: Literal["Published", "Draft"]


SAMPLE_COURSES: list[Course] = [
    {
        "id": 1,
        "title": "Intro to Python",
        "description": "A beginner-friendly introduction to Python programming.",
        "category": "Programming",
        "duration_hours": 40,
        "capacity": 30,
        "enrolled_students": 25,
        "instructor_id": 3,
        "status": "Published",
    },
    {
        "id": 2,
        "title": "Web Development Bootcamp",
        "description": "Master front-end and back-end web development.",
        "category": "Web Development",
        "duration_hours": 120,
        "capacity": 20,
        "enrolled_students": 18,
        "instructor_id": 2,
        "status": "Published",
    },
    {
        "id": 3,
        "title": "Data Science with Pandas",
        "description": "Learn data manipulation and analysis using the Pandas library.",
        "category": "Data Science",
        "duration_hours": 60,
        "capacity": 25,
        "enrolled_students": 25,
        "instructor_id": 1,
        "status": "Published",
    },
    {
        "id": 4,
        "title": "Advanced Machine Learning",
        "description": "Dive deep into advanced ML concepts and algorithms.",
        "category": "Data Science",
        "duration_hours": 80,
        "capacity": 15,
        "enrolled_students": 10,
        "instructor_id": 1,
        "status": "Published",
    },
    {
        "id": 5,
        "title": "UI/UX Design Fundamentals",
        "description": "Learn the principles of user interface and user experience design.",
        "category": "Design",
        "duration_hours": 50,
        "capacity": 20,
        "enrolled_students": 15,
        "instructor_id": 4,
        "status": "Draft",
    },
    {
        "id": 6,
        "title": "Cybersecurity Essentials",
        "description": "An introduction to cybersecurity threats and defense mechanisms.",
        "category": "IT & Security",
        "duration_hours": 45,
        "capacity": 25,
        "enrolled_students": 0,
        "instructor_id": 5,
        "status": "Draft",
    },
]


class CourseState(rx.State):
    courses: list[Course] = SAMPLE_COURSES
    search_query: str = ""
    category_filter: str = "All"
    view_mode: Literal["grid", "list"] = "grid"
    is_delete_dialog_open: bool = False
    course_to_delete: Optional[Course] = None
    is_form_modal_open: bool = False
    form_mode: Literal["add", "edit"] = "add"
    form_course: Course = {
        "id": 0,
        "title": "",
        "description": "",
        "category": "Programming",
        "duration_hours": 0,
        "capacity": 0,
        "enrolled_students": 0,
        "instructor_id": None,
        "status": "Draft",
    }

    @rx.var
    def filtered_courses(self) -> list[Course]:
        courses_list = self.courses
        if self.search_query:
            courses_list = [
                c
                for c in courses_list
                if self.search_query.lower() in c["title"].lower()
            ]
        if self.category_filter != "All":
            courses_list = [
                c for c in courses_list if c["category"] == self.category_filter
            ]
        return courses_list

    @rx.var
    def course_categories(self) -> list[str]:
        return sorted(list(set([c["category"] for c in self.courses])))

    @rx.event
    def set_view_mode(self, mode: Literal["grid", "list"]):
        self.view_mode = mode

    @rx.event
    def open_delete_dialog(self, course: Course):
        self.is_delete_dialog_open = True
        self.course_to_delete = course

    @rx.event
    def close_delete_dialog(self):
        self.is_delete_dialog_open = False
        self.course_to_delete = None

    @rx.event
    def delete_course(self):
        if self.course_to_delete:
            self.courses = [
                c for c in self.courses if c["id"] != self.course_to_delete["id"]
            ]
            self.close_delete_dialog()
            return rx.toast.success(
                f"Course '{self.course_to_delete['title']}' deleted."
            )

    @rx.var
    def course_to_delete_title(self) -> str:
        return self.course_to_delete["title"] if self.course_to_delete else ""

    @rx.event
    def open_add_modal(self):
        self.form_mode = "add"
        self.form_course = {
            "id": 0,
            "title": "",
            "description": "",
            "category": "Programming",
            "duration_hours": 0,
            "capacity": 10,
            "enrolled_students": 0,
            "instructor_id": None,
            "status": "Draft",
        }
        self.is_form_modal_open = True

    @rx.event
    def open_edit_modal(self, course: Course):
        self.form_mode = "edit"
        self.form_course = course
        self.is_form_modal_open = True

    @rx.event
    def close_form_modal(self):
        self.is_form_modal_open = False

    def _set_form_course_field(self, key: str, value):
        self.form_course[key] = value

    @rx.event
    def handle_form_change(self, field: str, value: str):
        if field in ["duration_hours", "capacity", "instructor_id"]:
            try:
                value = int(value)
            except (ValueError, TypeError) as e:
                import logging

                logging.exception(f"Error converting form value: {e}")
                value = None if field == "instructor_id" else 0
        self._set_form_course_field(field, value)

    @rx.event
    def save_course(self):
        if not self.form_course["title"]:
            return rx.toast.error("Course title is required.")
        if self.form_mode == "add":
            new_course = self.form_course.copy()
            new_course["id"] = (
                max((c["id"] for c in self.courses)) + 1 if self.courses else 1
            )
            self.courses.append(new_course)
            yield rx.toast.success(f"Course '{new_course['title']}' added.")
        else:
            self.courses = [
                self.form_course if c["id"] == self.form_course["id"] else c
                for c in self.courses
            ]
            yield rx.toast.success(f"Course '{self.form_course['title']}' updated.")
        self.close_form_modal()