password = input()
middle = ''
command = input()
while command != "Done":
    if command.startswith('TakeOdd'):
        for i in range(len(password)):
            if i % 2 != 0:
                middle += password[i]
        print( middle )
        password = middle
        middle = ''
    elif command.startswith('Cut'):
        _,index,length = command.split()
        index = int(index)
        length = int(length)
        sub = password[index:index+length]
        password = password.replace(sub, '', 1)
        print( password )
    elif command.startswith('Substitute'):
        _,substring,substitute = command.split()
        if substring in password:
            password = password.replace( substring, substitute )
            print( password )
        else:
            print("Nothing to replace!")
    command = input()
print( f"Your password is: {password}" )