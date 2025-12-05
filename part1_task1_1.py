# Task 1.1: Student Grade Manager

students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}")

def display_all():
    print("\nStudent Grades:")
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")

def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"\nAverage Grade: {avg:.2f}")
    else:
        print("No grades available.")

def highest_grade():
    if grades:
        print(f"Highest Grade: {max(grades)}")

# --- Main Program ---
while True:
    print("\n1. Add Student\n2. Display All\n3. Average Grade\n4. Highest Grade\n5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        average_grade()
    elif choice == "4":
        highest_grade()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
