
from Student import avg, max_grade, min_grade, check_status


def main():

    name = input("Enter student name: ")

    grades_input = input("Enter student grades: ")

    grades = [float(grade) for grade in grades_input.split()]

    average = avg(grades)
    maximum = max_grade(grades)
    minimum = min_grade(grades)

    status = check_status(average)

    print("\n========== Student Information ==========")

    print(f"Student: {name}")
    print(f"Avg = {average}")
    print(f"Max = {maximum}")
    print(f"Min = {minimum}")
    print(f"Status = {status}")

    print("=========================================")


if __name__ == "__main__":
    main()
