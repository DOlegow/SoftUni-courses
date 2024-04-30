stops = input()
command = ''
new_string = ''
removed_string = ''

while True:
    command = input()
    if command == 'Travel':
        break

    if (command.split(':'))[0] == 'Add Stop':
        action, index, destination = command.split(':')
        if len(stops) >= int(index):
            for i in range(int(index)):
                new_string += stops[i]
            new_string += destination + '-'
            stops_lst = stops.split('-')
            new_string += stops_lst[1]
            stops = new_string
    if (command.split(':'))[0] == 'Remove Stop':
        action, start_index, end_index = command.split ( ':' )
        if len(stops) >= int(start_index) and len(stops) >= int(end_index):
            for j in range(int(start_index)):
                new_string += stops[j]
            for k in range(int(end_index) + 1, len(stops)):
                new_string += stops[k]
            stops = new_string
print(stops)


