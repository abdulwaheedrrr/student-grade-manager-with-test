from student import Student
from grade_service import calculate_grade


def main():
    try:
        name = input("Enter student name: ").strip()

        marks_text = input(
            "Enter marks separated by spaces: "
        ).strip()

        marks = [float(value) for value in marks_text.split()]

        student = Student(name, marks)
        average = student.average()
        grade = calculate_grade(average)

        result= "passed" if grade != "F" else "failed"
        

        print("\n===== STUDENT REPORT =====")
        print(f"Name: {student.name}")
        print(f"Marks: {student.marks}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()