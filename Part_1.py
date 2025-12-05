# Part 1 — Basic Function Arguments (with user input)

def describe_pet(animal_type, pet_name):
    print(f"My pet is a {animal_type} and its name is {pet_name}.")

# Ask the user three times
print("\n--- Part 1: Describe Three Pets ---")
for i in range(1, 4):
    print(f"\nPet #{i}")
    animal = input("Enter the type of animal: ")
    name = input("Enter the pet's name: ")
    describe_pet(animal, name)
