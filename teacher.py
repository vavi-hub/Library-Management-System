from member import Member

class Teacher(Member):
    """A teacher who has library membership."""

    def __init__(self, name: str, age: int, contact: str, subject: str):
        super().__init__(name, age, contact)
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject cannot be empty.")
        self._subject = subject.strip()

    @property
    def subject(self):
        return self._subject

    def get_role(self):
        return "Teacher"

    def get_details(self):
        return f"{self.name} | ID: {self.member_id} | Subject: {self._subject}"


