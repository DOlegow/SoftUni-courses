def spaceship_game(input_parameter):
    commands = input_parameter.split("||")
    fuel = int(input())
    ammunition = int(input())

    for command in commands:
        unpack_command = command.split()
        action = unpack_command[0]

        if len(unpack_command) > 1:
            value = unpack_command[1]
        if action == "Travel":
            distance = int(value)
            fuel_needed = distance
            if fuel >= fuel_needed:
                fuel -= fuel_needed
                print(f"The spaceship travelled {distance} light-years.")
            else:
                print("Mission failed.")
                return
        elif action == "Enemy":
            enemy_armor = int(value)
            if ammunition >= enemy_armor:
                ammunition -= enemy_armor
                print(f"An enemy with {enemy_armor} armour is defeated.")
            elif ammunition < enemy_armor:
                fuel -= enemy_armor * 2
                if fuel >= 0:
                    print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
                else:
                    print("Mission failed.")
                    return

        elif action == "Repair":
            fuel_added = int(value)
            fuel += fuel_added
            ammunition += fuel_added * 2
            print(f"Ammunitions added: {fuel_added * 2}.")
            print(f"Fuel added: {fuel_added}.")
        elif action == "Titan":
            print("You have reached Titan, all passengers are safe.")
            return


parameter = input()
spaceship_game(parameter)
