def replace_ch(current_ch, new_ch, string):
    return string.replace(current_ch, new_ch)

if __name__ == "__main__":
    string = input()

    command = input()

    while command != 'Easter':
        command_parts = command.split()
        what_to_do = command_parts[0]

        if what_to_do == 'Replace':
            old_string = command_parts[1]
            new_string = command[2]
            string = replace_ch(old_string, new_string, string)
            print(string)
        elif what_to_do == 'Remove':
            old_string = command_parts[1]
            new_string = ''
            string = replace_ch(old_string, new_string, string)
            print(string)
        command = input()
