import reflex as rx
from typing import TypedDict, Literal
import datetime


class Enrollment(TypedDict):
    id: int
    student_id: int
    course_id: int
    enrollment_date: str
    status: Literal["Active", "Completed", "Dropped"]


class EnrollmentRow(TypedDict):
    id: int
    student_name: str
    course_name: str
    enrollment_date: str
    status: Literal["Active", "Completed", "Dropped"]


SAMPLE_ENROLLMENTS: list[Enrollment] = [
    {
        "id": 1,
        "student_id": 1,
        "course_id": 1,
        "enrollment_date": "2023-01-15",
        "status": "Completed",
    },
    {
        "id": 2,
        "student_id": 1,
        "course_id": 2,
        "enrollment_date": "2023-03-01",
        "status": "Active",
    },
    {
        "id": 3,
        "student_id": 2,
        "course_id": 1,
        "enrollment_date": "2023-01-15",
        "status": "Active",
    },
    {
        "id": 4,
        "student_id": 3,
        "course_id": 3,
        "enrollment_date": "2023-02-20",
        "status": "Dropped",
    },
    {
        "id": 5,
        "student_id": 4,
        "course_id": 4,
        "enrollment_date": "2023-04-10",
        "status": "Active",
    },
    {
        "id": 6,
        "student_id": 5,
        "course_id": 2,
        "enrollment_date": "2023-03-01",
        "status": "Active",
    },
    {
        "id": 7,
        "student_id": 7,
        "course_id": 1,
        "enrollment_date": "2023-01-15",
        "status": "Completed",
    },
    {
        "id": 8,
        "student_id": 8,
        "course_id": 3,
        "enrollment_date": "2023-02-20",
        "status": "Active",
    },
]


class EnrollmentState(rx.State):
    enrollments: list[Enrollment] = SAMPLE_ENROLLMENTS

    @rx.var
    async def enrollment_rows(self) -> list[EnrollmentRow]:
        from app.states.student_state import StudentState
        from app.states.course_state import CourseState

        student_state = await self.get_state(StudentState)
        course_state = await self.get_state(CourseState)
        student_map = {s["id"]: s["name"] for s in student_state.students}
        course_map = {c["id"]: c["title"] for c in course_state.courses}
        rows = []
        for e in self.enrollments:
            rows.append(
                {
                    "id": e["id"],
                    "student_name": student_map.get(e["student_id"], "Unknown Student"),
                    "course_name": course_map.get(e["course_id"], "Unknown Course"),
                    "enrollment_date": e["enrollment_date"],
                    "status": e["status"],
                }
            )
        return rows