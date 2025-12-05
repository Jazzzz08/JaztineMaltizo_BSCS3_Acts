# Part 5 — Mini Challenge (Calculator with Loop + User Input)

def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"


print("\n--- Part 5: Mini Calculator (Loop Version) ---")

while True:  # loop so calculator can be reused
    op = input("\nChoose operation (add / multiply / subtract): ").lower()
    n1 = float(input("Enter first number: "))

    use_default = input("Use default second number (1)? yes/no: ").lower()

    if use_default == "yes":
        print("Result:", compute(op, n1))
    else:
        n2 = float(input("Enter second number: "))
        print("Result:", compute(op, n1, n2))

    # Ask user if they want to calculate again
    again = input("\nDo you want to perform another calculation? yes/no: ").lower()
    if again != "yes":
        print("Calculator ended. Goodbye!")
        break
