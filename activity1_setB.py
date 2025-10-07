
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

def print_formatted_info(title, **kwargs):
    print(title.upper())
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# -----------------------------------

print("\n--- Text and Number Analyzer ---")

# Task 1
text = input("\nEnter a word or phrase to check if it's a palindrome: ")
print(f"Is palindrome? {is_palindrome(text)}")

# Task 2
score_input = float(input("\nEnter a score (0-100) to get the grade: "))
print(f"Your grade is: {get_grade(score_input)}")

# Task 3
numbers = input("\nEnter numbers separated by spaces to multiply: ").split()
numbers = [float(n) for n in numbers]
print(f"The product is: {multiply_all(*numbers)}")

# Task 4
print("\n--- Create a formatted report ---")
title = input("Enter a report title: ")
num_items = int(input("How many pieces of information will you add? "))

info = {}
for _ in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    info[key] = value

print("\nFormatted Report:")
print_formatted_info(title, **info)
