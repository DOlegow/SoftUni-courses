raw_activation_key = input()
string_with_instructions = input()
while string_with_instructions != 'Generate':
    list_of_instructions = string_with_instructions.split('>>>')
    command = list_of_instructions[0]
    if command == 'Contains':
        substring = list_of_instructions[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command == 'Flip':
        case = list_of_instructions[1]


    command = input()