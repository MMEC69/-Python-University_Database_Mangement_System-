from course import Course
from student import Student
from datetime import datetime
class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise ValueError("Invalid student...")

        if not isinstance(course, Course):
            raise ValueError("Invalid course...")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()