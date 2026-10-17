def calculate_grade(average):
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100.")

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"