import reflex as rx
from typing import TypedDict


class EnrollmentData(TypedDict):
    month: str
    enrollments: int


class CoursePopularityData(TypedDict):
    name: str
    students: int


class Activity(TypedDict):
    icon: str
    description: str
    timestamp: str


class DashboardState(rx.State):
    """State for the dashboard page."""

    total_students: int = 1250
    active_courses: int = 48
    total_teachers: int = 75
    enrollment_rate: float = 85.6
    enrollment_trend: list[EnrollmentData] = [
        {"month": "Jan", "enrollments": 150},
        {"month": "Feb", "enrollments": 220},
        {"month": "Mar", "enrollments": 180},
        {"month": "Apr", "enrollments": 270},
        {"month": "May", "enrollments": 250},
        {"month": "Jun", "enrollments": 310},
    ]
    course_popularity: list[CoursePopularityData] = [
        {"name": "Intro to Python", "students": 120},
        {"name": "Web Development", "students": 95},
        {"name": "Data Science", "students": 80},
        {"name": "Machine Learning", "students": 70},
        {"name": "UI/UX Design", "students": 60},
    ]
    recent_activities: list[Activity] = [
        {
            "icon": "user-plus",
            "description": "New student 'John Doe' was registered.",
            "timestamp": "5m ago",
        },
        {
            "icon": "clipboard-list",
            "description": "'Intro to Python' course has 5 new enrollments.",
            "timestamp": "1h ago",
        },
        {
            "icon": "book-open-check",
            "description": "New course 'Advanced React' has been published.",
            "timestamp": "3h ago",
        },
        {
            "icon": "user-plus",
            "description": "New student 'Jane Smith' was registered.",
            "timestamp": "1d ago",
        },
    ]