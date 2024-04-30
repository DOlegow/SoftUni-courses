def spaceship_game(input_string):
    commands = input_string.split("| |")
    route = commands[0]
    fuel = int(commands[1])
    ammunition = int(commands[2])

    for command in route.split("|"):
        action, value = command.strip().split()
        if action == "Travel":
            distance = int(value)
            fuel_needed = distance
            if fuel >= fuel_needed:
                fuel -= fuel_needed
                print(f"The spaceship traveled {distance} light-years.")
            else:
                print("Mission failed.")
                return
        elif action == "Enemy":
            enemy_armor = int(value)
            if ammunition >= enemy_armor:
                ammunition -= enemy_armor
                print(f"An enemy with {enemy_armor} armor is defeated.")
            elif fuel >= enemy_armor * 2:
                fuel -= enemy_armor * 2
                print(f"An enemy with {enemy_armor} armor is outmaneuvered.")
            else:
                print("Mission failed.")
                return
        elif action == "Repair":
            fuel_added, ammunition_added = map(int, value.split())
            fuel += fuel_added
            ammunition += ammunition_added * 2
            print(f"Ammunitions added: {ammunition_added}.")
            print(f"Fuel added: {fuel_added}.")
        elif action == "Titan":
            print("You have reached Titan, all passengers are safe.")
            return


input_str = "Travel 10| |Enemy 30| |Repair 15| |Titan\n50\n80"
spaceship_game(input_str)
