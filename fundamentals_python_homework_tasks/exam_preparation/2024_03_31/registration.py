username = input()
commands = input()
while commands != 'Registration':
    if commands.startswith('Letters'):
        _,command = commands.split()
        if command == 'Lower':
            username = username.lower()
            print(username)
        elif command == 'Upper':
            username = username.upper()
            print ( username)
    elif commands.startswith('Reverse'):
        _,start_index,end_index = commands.split()
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index >= 0 and start_index <= len(username):
            if end_index >= 0 and end_index <= len(username):
                reversed_string = username[start_index:end_index+1][::-1]
                if reversed_string:
                    print(reversed_string)
    elif commands.startswith('Substring'):
        _,substring = commands.split()
        if substring in username:
            username = username.replace(substring,'')
            print ( username )
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif commands.startswith('Replace'):
        _,char = commands.split()
        username = username.replace(char, '-')
        print(username)
    elif commands.startswith('IsValid'):
        _, char = commands.split()
        if char in username:
            print('Valid username.')
        else:
            print(f"{char} must be contained in your username.")

    commands = input()