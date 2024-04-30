travel_route_to_Titan_string = input()
fuel = int(input())
ammunition = int(input())

list_of_commands = travel_route_to_Titan_string.split('||')
for command in list_of_commands:
    command = list_of_commands[0].split ( ' ' )
    distance = int ( command[1] )
    if command[0] == 'Travel':
        if fuel >= distance:
            print ( f'The spaceship traveled {distance} light-years.' )
            fuel -= distance
            continue
        elif fuel < distance:
            print ( 'Mission failed' )
            break
    elif command[0] == 'Enemy':
        enemy_armour = int ( command[1] )
        if ammunition >= enemy_armour:
            print(f"An enemy with {enemy_armour} armour is defeated.")
            ammunition -= enemy_armour
