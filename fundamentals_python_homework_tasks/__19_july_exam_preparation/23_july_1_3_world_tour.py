places = input()

while True:
    command = input()
    if command == "Travel":
        break

    first_command, second_command, third_command = command.split(':')

    if first_command == 'Add Stop':
        if int(second_command) < len(places):
            part_one = places[:int(second_command)]
            part_two = places[int(second_command):]
            places = part_one + third_command + part_two

        print(places)

    if first_command == 'Remove Stop':
        if int(second_command) < len(places) and int(third_command) < len(places):
            part_one = places[:int(second_command)]
            part_two = places[int(third_command)+1:]
            places = part_one + part_two

        print(places)

    if first_command == 'Switch':
        if second_command in places:
            places = places.replace(second_command, third_command)
        print(places)

print(f'Ready for world tour! Planned stops: {places}')
