class Student:
    def __init__(self, name, marks):
        if not name.strip():
            raise ValueError("Student name cannot be empty.")

        if not marks:
            raise ValueError("At least one mark is required.")

        for mark in marks:
            if not isinstance(mark, (int, float)) or isinstance(mark, bool):
                raise ValueError("Marks must be numbers.")

            if not 0 <= mark <= 100:
                raise ValueError("Marks must be between 0 and 100.")

        self.name = name.strip()
        self.marks = list(marks)

    def average(self):
        return sum(self.marks) / len(self.marks)