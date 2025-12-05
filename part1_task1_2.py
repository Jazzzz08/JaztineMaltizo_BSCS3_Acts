# Task 1.2: List Operations Practice (User Input Version)

# Ask user for numbers
user_input = input("Enter numbers separated by spaces: ")

# Convert input string into a list of integers
numbers = [int(num) for num in user_input.split()]

print(f"\nOriginal list: {numbers}")

# Sort the list
numbers.sort()
print(f"Sorted list: {numbers}")

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)

# Display results
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"List Length: {len(numbers)}")
