from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise ValueError("Invalid Address...")
        else:
            raise ValueError("Invalid Address...")

    def add_address(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError("Invalid Address...")

        self.professors.append(professor)

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError("Invalid Professor...")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError("Invalid Enroll")

        if len(self.enrollments) == self.max:
            raise ValueError("Cannot enroll, course is full...")

        self.enrollments.append(enroll)

    def is_canceled(self):
        return len(self.enrollments) < self.min