# Part 4 — Create Your Own Function

def order_drink(drink, size="medium", iced=False):
    temp = "iced" if iced else "hot"
    return f"Your order: {size} {temp} {drink}"

print("\n--- Part 4: Drink Ordering System ---")

# Default drink
drink1 = input("Enter a drink (default medium & hot): ")
print(order_drink(drink1))

# Large hot chocolate
drink2 = input("Enter a drink for large hot order: ")
print(order_drink(drink2, size="large"))

# Custom iced milktea drink
drink3 = input("Enter drink for iced order: ")
size3 = input("Enter size (small/medium/large): ")
print(order_drink(drink3, size=size3, iced=True))
