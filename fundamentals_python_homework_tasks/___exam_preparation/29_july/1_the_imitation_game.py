txt = input()
txt_list = []

for ch in txt:
    txt_list.append(ch)

while True:
    command = input ()
    if command == "Decode":
        break

    action, *args = command.split("|")

    if action == 'Move':
        if args[0].isdigit():
            n = int(args[0])
            for element in range ( n ):
                letter = txt_list.pop ( 0 )
                txt_list.append ( letter )
        else:
            continue

    if action == 'Insert':
        if args[0].isdigit ():
            insert_index = int(args[0])
            txt_list.insert ( insert_index, args[1] )
        else:
            continue


    if action == 'ChangeAll':
        for i in range(len(txt_list) - 1, -1, -1 ):
            if txt_list[i] == args[0]:
                txt_list[i] = args[1]


print(f'The decrypted message is: {"".join(txt_list)}')
