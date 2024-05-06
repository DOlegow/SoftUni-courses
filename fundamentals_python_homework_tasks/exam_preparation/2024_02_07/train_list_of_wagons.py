number_of_wagons = int(input())
command_people = input()
train = [0] * number_of_wagons
while command_people != 'End':
    command_parts = command_people.split(' ')
    if command_parts[0] == 'add':
        train[-1] += int(command_parts[1])
    elif command_parts[0] == 'insert':
        train[int(command_parts[1])] +=  int(command_parts[2])
    elif command_parts[0] == 'leave':
        train[int(command_parts[1])] -= int(command_parts[2])
    command_people = input()
print(train)