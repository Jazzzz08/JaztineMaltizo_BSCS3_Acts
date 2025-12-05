import pickle

# Task 4.1: Student Records File System

filename = "students.pkl"

def save_records(data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print("Records saved successfully!")

def load_records():
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No record file found.")
        return {}

def export_to_text(data):
    with open("students.txt", 'w') as f:
        for sid, info in data.items():
            f.write(f"{sid}: {info}\n")
    print("Exported to students.txt")

students = load_records()

while True:
    print("\n1. Add Student\n2. Save\n3. Load\n4. Export to Text\n5. Display All\n6. Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        sid = input("ID: ")
        name = input("Name: ")
        grade = input("Grade: ")
        major = input("Major: ")
        students[sid] = {'name': name, 'grade': grade, 'major': major}
    elif ch == "2":
        save_records(students)
    elif ch == "3":
        students = load_records()
    elif ch == "4":
        export_to_text(students)
    elif ch == "5":
        print(students)
    elif ch == "6":
        break
