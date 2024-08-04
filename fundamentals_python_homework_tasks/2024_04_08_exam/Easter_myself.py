original_string = input()
command = input()
current_string = ''
while command != "Easter":
    command = command.split()

    if command[0] == "Replace":
        current_sring = original_string.replace(command[1], command[2])
        print(current_sring)
    elif command[0] == "Remove":
        current_string = original_string.replace(command[1], '')
        print(current_string)
    elif command[0] == "Includes":
        if command[1] in current_string:
            print("True")
        else:
            print("False")
    elif command[0] == "Change":
        if command[1] == "Lower":
            current_string = current_string.lower()
            print(current_string)
        elif command[1] == "Upper":
            current_string = current_string.upper()
            print(current_string)
    elif command[0] == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if current_string:
            if 0 <= start_index <= end_index <= len(current_string):
                substring = current_string[start_index:end_index+1]
                reversed_substring = substring[::-1]
                print(reversed_substring)
        else:
            if 0 <= start_index <= end_index <= len(original_string):
                substring = original_string[start_index:end_index + 1]
                reversed_substring = substring[::-1]
                print(reversed_substring)
    command = input()