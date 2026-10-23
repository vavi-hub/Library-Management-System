from member import Member

class Student(Member):
    """A student who has library membership."""

    def __init__(self, name: str, age: int, contact: str, course: str):
        super().__init__(name, age, contact)
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course cannot be empty.")
        self._course = course.strip()

    @property
    def course(self):
        return self._course

    def get_role(self):
        return "Student"

    def get_details(self):
        return f"{self.name} | ID: {self.member_id} | Course: {self._course}"
