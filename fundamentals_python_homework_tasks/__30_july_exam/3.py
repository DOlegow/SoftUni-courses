def add(animals, areas, animal_name, needed_food_quantity, area):
    if animal_name not in animals:
        animals[animal_name] = 0
    animals[animal_name] += needed_food_quantity

    if area not in areas:
        areas[area] = []
    areas[area].append(animal_name)


def feed_animal(animals, areas, animal_name, food):
    if animal_name in animals:
        animals[animal_name] -= food
        if animals[animal_name] <= 0:
            del animals[animal_name]
            for area, animals_in_area in areas.items():
                if animal_name in animals_in_area:
                    animals_in_area.remove(animal_name)
                    break
            print(f"{animal_name} was successfully fed")


def print_animals(animals):
    print("Animals:")
    for animal_name, needed_food_quantity in sorted(animals.items(), key=lambda x: (-x[1], x[0])):
        print(f" {animal_name} -> {needed_food_quantity}g")


def print_hungry_animals(areas):
    print("Areas with hungry animals:" )
    for area, animals_in_area in sorted(areas.items()):
        number_of_hungry_animals = sum(1 for animal in animals_in_area if (animal in animals_in_area and int(animals[animal])) > 0)
        if number_of_hungry_animals > 0:
            print(f" {area}: {number_of_hungry_animals}")


def zoo_feeding():
    animals = {}
    areas = {}

    while True:
        command = input().strip()
        if command == "EndDay":
            break

        if command.startswith("Add"):
            _, params = command.split(": ")
            animal_name, needed_food_quantity, area = params.split("-")
            needed_food_quantity = int(needed_food_quantity)
            add(animals, areas, animal_name, needed_food_quantity, area)

        elif command.startswith("Feed"):
            _, params = command.split(": ")
            animal_name, food = params.split("-")
            food = int(food)
            feed_animal(animals, areas, animal_name, food)

    print_animals(animals)
    print_hungry_animals(areas)


zoo_feeding()
