# Task 4.2: File Operations Practice

filename = "sample.txt"

# Write mode
with open(filename, 'w') as f:
    f.write("This is a new file.\n")
print("Written to file.")

# Read mode
try:
    with open(filename, 'r') as f:
        print("\nFile Contents:")
        print(f.read())
except FileNotFoundError:
    print("File not found.")

# Append mode
with open(filename, 'a') as f:
    f.write("This line is appended.\n")
print("\nAppended new content.")

# Read again
with open(filename, 'r') as f:
    print("\nUpdated File Contents:")
    print(f.read())
