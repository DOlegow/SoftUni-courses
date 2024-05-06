string_with_message = input()
string_with_instructions = input()
while string_with_instructions != "Reveal":
    if string_with_instructions.startswith("InsertSpace"):
        command, index = string_with_instructions.split(":|:")
        string_with_message = string_with_message[:int(index)] + ' ' + string_with_message[int(index):]
        print ( string_with_message )
    elif string_with_instructions.startswith("Reverse"):
        command, substring = string_with_instructions.split(":|:")
        if substring in string_with_message:
            string_with_message = string_with_message.replace(substring, '', 1)
            string_with_message = string_with_message + substring[::-1]
            print(string_with_message)
        elif substring not in string_with_message:
             print("error")
    elif string_with_instructions.startswith("ChangeAll"):
        command, substring, replacement = string_with_instructions.split(':|:')
        string_with_message = string_with_message.replace(substring, replacement)
        print(string_with_message)
    string_with_instructions = input()
print(f"You have a new text message: {string_with_message}")
