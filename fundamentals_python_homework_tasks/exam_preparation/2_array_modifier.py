array = list(map(int, input().split()))

command = input()
while command != "end":
    command_args = command.split()

    if command_args[0] == "swap":
        index1 = int(command_args[1])
        index2 = int(command_args[2])
        array[index1], array[index2] = array[index2], array[index1]
    elif command_args[0] == "multiply":
        index1 = int(command_args[1])
        index2 = int(command_args[2])
        array[index1] *= array[index2]
    elif command_args[0] == "decrease":
        array = [num - 1 for num in array]

    command = input()

result = ', '.join(map(str, array))
print(result)
