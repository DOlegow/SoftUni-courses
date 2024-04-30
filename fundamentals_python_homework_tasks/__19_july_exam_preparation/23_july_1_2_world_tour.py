stops = input()
stop_list = []
new_stops = ''
for ch in stops:
    stop_list.append(ch)

while True:
    command = input()
    if command == 'Travel':
        break
    action, index, destination = command.split (':')
    if action == 'Add Stop':
        if len(stops) >= int(index):
            for i in range(len(destination), 0, -1):
                stop_list.insert(int(index), destination[i-1])
        print ( ''.join ( stop_list ) )
    action, start_index, end_index = command.split(':')
    if action == 'Remove Stop':
        if len(stops) >= int(start_index) and len(stops) >= int(end_index):
            a = int(end_index) + 1 - int(start_index)
            while a > 0:
                stop_list.remove(stop_list[int(start_index)])
                a -= 1
            print(''.join(stop_list))
    action, old_string, new_string = command.split(':')
    new_stops = ''.join(stop_list)
    if action == 'Switch':
        if old_string in new_stops:
            new_stops = new_stops.replace(old_string, new_string)
        print(new_stops)
if new_stops:
    stops = new_stops
print(f'Ready for world tour! Planned stops: {stops}')
