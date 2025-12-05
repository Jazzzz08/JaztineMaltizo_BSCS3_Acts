# Part 2 — Positional and Keyword Arguments (user input)

def describe_pet(animal_type, pet_name):
      print(f"My pet is a {animal_type} and its name is {pet_name}.")

print("\n--- Part 2: Positional vs Keyword Arguments ---")

# Positional input
pos_animal = input("Enter animal (positional): ")
pos_name = input("Enter name (positional): ")
describe_pet(pos_animal, pos_name)  # positional

# Keyword input (order switched)
key_pet_name = input("Enter pet name (keyword): ")
key_animal_type = input("Enter animal type (keyword): ")
describe_pet(pet_name=key_pet_name, animal_type=key_animal_type)
