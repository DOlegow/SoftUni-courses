def replace_ch(current_char, new_char, string):
    return string.replace(current_char, new_char)

def remove_substring(substring, string):
    return string.replace(substring, "")

def includes_string(substring, string):
    return "True" if substring in string else "False"

def changecase(command, string):
    if command == "Lower":
        return string.lower()
    elif command == "Upper":
        return string.upper()

def reverse_substring(start_index, end_index, string):
    if 0 <= start_index < len(string) and 0 <= end_index < len(string):
        substring = string[start_index:end_index+1]
        return substring[::-1]
    else:
        return None

if __name__ == "__main__":
    string = input()

    command = input()
    while command != "Easter":
        command_parts = command.split()
        what_to_do = command_parts[0]

        if what_to_do == "Replace":
            current_char = command_parts[1]
            new_char = command_parts[2]
            string = replace_ch( current_char, new_char, string )
            print(string)
        elif what_to_do == "Remove":
            substring = command_parts[1]
            string = remove_substring(substring, string)
            print(string)
        elif what_to_do == "Includes":
            substring = command_parts[1]
            print(includes_string(substring, string))
        elif what_to_do == "Change":
            case = command_parts[1]
            string = changecase( case, string )
            print(string)
        elif what_to_do == "Reverse":
            start_index = int(command_parts[1])
            end_index = int(command_parts[2])
            reversed_substring = reverse_substring(start_index, end_index, string)
            if reversed_substring is not None:
                print(reversed_substring)
        command = input()
