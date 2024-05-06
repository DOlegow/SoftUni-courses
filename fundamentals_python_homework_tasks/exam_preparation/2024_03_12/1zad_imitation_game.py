txt = input()

while True:
    command = input ()
    if command == "Decode":
        break

    action, *args = command.split("|")

    if action == 'Move':
        if args[0].isdigit():
            n = int(args[0])
            txt = txt[n:] + txt[:n]

    elif action == 'Insert':
        if args[0].isdigit ():
            insert_index = int(args[0])
            txt = txt[:insert_index] + args[1] + txt[insert_index:]

    elif action == 'ChangeAll':
        a = args[0]
        b = args[1]
        txt = txt.replace(a,b)



print(f'The decrypted message is: {txt}')