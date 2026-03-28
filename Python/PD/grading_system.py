def get_grade(score):
    """
    Converts a numerical score (0-100) to a letter grade.
    """
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

# Main part of the program
if __name__ == "__main__":
    try:
        # Get user input and convert it to a float to handle decimals
        marks = float(input("Please enter the marks (0-100): "))

        # Validate the marks are within a plausible range (0-100)
        if 0 <= marks <= 100:
            grade = get_grade(marks)
            print(f"Grade: {grade}")
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

    except ValueError:
        # Handle cases where the user enters non-numeric input
        print("Invalid input. Please enter a numeric value.")
