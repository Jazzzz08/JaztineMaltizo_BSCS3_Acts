"""
===========================================================
 LABORATORY ACTIVITY: Regular Expression & Python OOP 
===========================================================
"""

import re

# ===========================================================
# PART 1 — REGULAR EXPRESSION TASKS
# ===========================================================

# ------------------------------
# TASK 1: Extract Student Data
# ------------------------------
print("\n=== PART 1 — TASK 1: Extract Student Data Using Regex ===")

data = input("Enter student raw data:\n")

pattern = r"ID:\s?(?P<id>\d{4}-\d{3})\s?\|\s?Name:\s?(?P<name>[A-Za-z\s]+)\s?\|\s?Email:\s?(?P<email>[^\s]+)\s?\|\s?Age:\s?(?P<age>\d+)"

match = re.search(pattern, data)

if match:
    print("\nExtracted Data:")
    print("ID:", match.group("id"))
    print("Name:", match.group("name"))
    print("Email:", match.group("email"))
    print("Age:", match.group("age"))
else:
    print("Invalid format!")


# ------------------------------
# TASK 2: Validate Email
# ------------------------------
print("\n=== PART 1 — TASK 2: Validate Email Format ===")

email = input("Enter an email to validate: ")

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# ------------------------------
# TASK 3: Mask Email Username
# ------------------------------
print("\n=== PART 1 — TASK 3: Mask Email Username ===")

email = input("Enter an email to mask: ")

masked = re.sub(r"^[^@]+", "*****", email)
print("Masked Email:", masked)


# ------------------------------
# TASK 4: Find Words in a Name
# ------------------------------
print("\n=== PART 1 — TASK 4: Find All Words in a Name ===")

name = input("Enter a full name: ")

words = re.findall(r"[A-Za-z]+", name)

print("Words found:", words)


# ===========================================================
# PART 2 — PYTHON OOP TASKS
# ===========================================================

# ------------------------------
# TASK 5: Simple Student Class
# ------------------------------
print("\n=== PART 2 — TASK 5: Create a Student Class ===")

class Student:
    def __init__(self, student_id, name, email, age):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age

sid = input("Enter ID: ")
name = input("Enter Name: ")
email = input("Enter Email: ")
age = input("Enter Age: ")

s = Student(sid, name, email, age)

print("\nStudent Created:")
print("ID:", s.student_id)
print("Name:", s.name)
print("Email:", s.email)
print("Age:", s.age)


# ------------------------------
# TASK 6: Encapsulation + Getter/Setter
# ------------------------------
print("\n=== PART 2 — TASK 6: Encapsulation (Private Attributes) ===")

class StudentEncap:
    def __init__(self, student_id, name, email, age):
        self.student_id = student_id
        self.name = name
        self.__email = email
        self.__age = age

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w+$", new_email):
            self.__email = new_email
            print("Email updated successfully!")
        else:
            print("Invalid email format!")

sid = input("\nEnter ID: ")
name = input("Enter Name: ")
email = input("Enter Email: ")
age = input("Enter Age: ")

se = StudentEncap(sid, name, email, age)

print("\nCurrent Email:", se.get_email())
new_email = input("Enter new email to update: ")
se.set_email(new_email)

print("Final Email:", se.get_email())


# ------------------------------
# TASK 7: Multiple Objects with Regex
# ------------------------------
print("\n=== PART 2 — TASK 7: Multiple Student Objects ===")

student_records = []

count = int(input("How many students will you enter? "))

for i in range(count):
    print(f"\nEnter student #{i+1} (raw format):")
    raw = input()

    match = re.search(pattern, raw)

    if match:
        s = Student(
            match.group("id"),
            match.group("name"),
            match.group("email"),
            match.group("age")
        )
        student_records.append(s)
    else:
        print("Invalid format! Entry skipped.")

print("\nStored Students:")
for s in student_records:
    print(f"{s.student_id} - {s.name} - {s.email} - {s.age}")


# ------------------------------
# TASK 8: Inheritance — Scholar
# ------------------------------
print("\n=== PART 2 — TASK 8: Inheritance (Scholar Class) ===")

class Scholar(Student):
    def __init__(self, student_id, name, email, age, scholarship_type):
        super().__init__(student_id, name, email, age)
        self.scholarship_type = scholarship_type

    def display_scholar_info(self):
        print("\nScholar Information:")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Scholarship:", self.scholarship_type)

sid = input("Enter ID: ")
name = input("Enter Name: ")
email = input("Enter Email: ")
age = input("Enter Age: ")
sch_type = input("Enter Scholarship Type: ")

sch = Scholar(sid, name, email, age, sch_type)
sch.display_scholar_info()


# ===========================================================
# PART 3 — FULL SYSTEM INTEGRATION
# ===========================================================

print("\n=== PART 3 — TASK 9: Full System Integration ===")

class StudentFinal:
    def __init__(self, student_id, name, email, age):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

class ScholarFinal(StudentFinal):
    def __init__(self, student_id, name, email, age, scholarship_type):
        super().__init__(student_id, name, email, age)
        self.scholarship_type = scholarship_type

    def display(self):
        super().display()
        print(f"Scholarship: {self.scholarship_type}")

student_records_final = []

count = int(input("How many final student entries? "))

for i in range(count):
    print(f"\nEnter raw data for student #{i+1}:")
    raw = input()

    match = re.search(pattern, raw)
    if not match:
        print("Invalid entry! Skipped.")
        continue

    sid = match.group("id")
    name = match.group("name")
    email = match.group("email")
    age = match.group("age")

    is_sch = input("Is this student a scholar? (yes/no): ").lower()

    if is_sch == "yes":
        sch_type = input("Enter scholarship type: ")
        obj = ScholarFinal(sid, name, email, age, sch_type)
    else:
        obj = StudentFinal(sid, name, email, age)

    student_records_final.append(obj)

print("\n=== FINAL OUTPUT ===")
for s in student_records_final:
    s.display()
    print("-------------------------")
