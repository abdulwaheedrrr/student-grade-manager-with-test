import unittest

from student import Student
from grade_service import calculate_grade


class TestStudent(unittest.TestCase):

    def test_average(self):
        student = Student("Ali", [80, 90, 70])
        self.assertEqual(student.average(), 80)

    def test_student_name_is_trimmed(self):
        student = Student(" Ali ", [80])
        self.assertEqual(student.name, "Ali")

    def test_empty_name_is_rejected(self):
        with self.assertRaises(ValueError):
            Student(" ", [80])

    def test_empty_marks_are_rejected(self):
        with self.assertRaises(ValueError):
            Student("Ali", [])

    def test_out_of_range_marks_are_rejected(self):
        with self.assertRaises(ValueError):
            Student("Ali", [120])

    def test_invalid_mark_type_is_rejected(self):
        with self.assertRaises(ValueError):
            Student("Ali", ["eighty"])

    def test_grade_boundaries(self):
        self.assertEqual(calculate_grade(90), "A")
        self.assertEqual(calculate_grade(80), "B")
        self.assertEqual(calculate_grade(70), "C")
        self.assertEqual(calculate_grade(60), "D")
        self.assertEqual(calculate_grade(59), "F")

    def test_invalid_average_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_grade(101)


if __name__ == "__main__":
    unittest.main()