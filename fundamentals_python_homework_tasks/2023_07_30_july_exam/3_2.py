animals = {}
areas = {}
hungry_animals = 0

while True:
    command = input()

    if command == "EndDay":
        break

    elif command.startswith("Add:"):
        command_first_part, command_remain = command.split(":")
        animal_name, needed_food_quantity, area = command_remain.split("-")
        needed_food_quantity = int ( needed_food_quantity )
        if animal_name in animals:
            needed_food_quantity += animals[animal_name]['food_limit']

        animals[animal_name] = {"food_limit": needed_food_quantity, "area": area.strip()}


    elif command.startswith("Feed:"):
        command_first_part, command_remain = command.split(":")
        animal_name, food = command_remain.split("-")
        food = int(food)

        if animal_name in animals:
            animals[animal_name]["food_limit"] -= food

            if animals[animal_name]["food_limit"] <= 0:
                print(f"{animal_name} was successfully fed")
                del animals[animal_name]
print("Animals:")
for animal_name, animal_data in animals.items():
    print(f"{animal_name} -> {animal_data['food_limit']}g")

for i in range(0, len(animals) + 1, 2):
    if animals[animal_name]['food_limit'] > 0:
        area = animals[animal_name]['area']
        hungry_animals += 1
        areas[area] = hungry_animals
print("Areas with hungry animals:")
for area, count_of_hungry_animals in areas.items():
    print(f"{area}: {areas[area]}")