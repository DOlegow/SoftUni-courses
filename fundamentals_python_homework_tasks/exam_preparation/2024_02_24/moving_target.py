# input data
the_sequence_of_targets = input()
strings_targets = []
# making list of numbers(targets)
list_of_targets = the_sequence_of_targets.split(' ')

# convert elements of list_of_targets to int
numbers_list_of_targets = list(map(int, list_of_targets))
# receive command
command_and_data = input()

while command_and_data != 'End':
    list_command_and_data = command_and_data.split(' ')

    command = list_command_and_data[0]
    if command == 'Shoot':
        index = int(list_command_and_data[1])
        power = int(list_command_and_data[2])
        if 0 <= index < len(numbers_list_of_targets):
            numbers_list_of_targets[index] -= power
            if numbers_list_of_targets[index] <= 0:
                numbers_list_of_targets.remove(numbers_list_of_targets[index])
    elif command == 'Add':
        index = int ( list_command_and_data[1] )
        value = int ( list_command_and_data[2] )
        if 0 <= index < len(numbers_list_of_targets):
            numbers_list_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == 'Strike':
        index = int ( list_command_and_data[1] )
        radius = int ( list_command_and_data[2] )
        if 0 <= (index + radius) < len(numbers_list_of_targets) and 0 <= (index - radius) < len(numbers_list_of_targets):
            begin_removing = index - radius
            end_removing = index + radius
            for i in range(end_removing, begin_removing - 1, -1):
                numbers_list_of_targets.remove(numbers_list_of_targets[i])
        else:
            print("Strike missed!")

    command_and_data = input()
for i in range (len(numbers_list_of_targets)):
    current_number = str (numbers_list_of_targets[i])
    strings_targets.append ( current_number )
print('|'.join(strings_targets))