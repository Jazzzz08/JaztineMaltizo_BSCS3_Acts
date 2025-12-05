# Task 3.1: Student Database

students = {}

def add_student():
    sid = input("Enter student ID: ")
    name = input("Enter name: ")
    grade = input("Enter grade: ")
    major = input("Enter major: ")
    students[sid] = {'name': name, 'grade': grade, 'major': major}
    print(f"Added student {name}")

def get_student():
    sid = input("Enter student ID to retrieve: ")
    if sid in students:
        print(students[sid])
    else:
        print("Student not found.")

def update_grade():
    sid = input("Enter student ID to update: ")
    if sid in students:
        new_grade = input("Enter new grade: ")
        students[sid]['grade'] = new_grade
        print("Grade updated.")
    else:
        print("Student not found.")

def display_all():
    for sid, info in students.items():
        print(f"{sid}: {info}")

while True:
    print("\n1. Add Student\n2. Retrieve Student\n3. Update Grade\n4. Display All\n5. Exit")
    ch = input("Enter choice: ")
    if ch == "1": add_student()
    elif ch == "2": get_student()
    elif ch == "3": update_grade()
    elif ch == "4": display_all()
    elif ch == "5": break
    else: print("Invalid choice.")
