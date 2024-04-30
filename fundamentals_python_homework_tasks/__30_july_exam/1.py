txt = input()

while True:
    command = input()
    if command == "Done":
        break

    if command.startswith("Change"):
        action, ch, replacement = command.split()
        txt = txt.replace(ch, replacement)
        print(txt)

    elif command.startswith("Includes"):
        action, substring = command.split()
        if substring in txt:
            print("True")
        else:
            print("False")

    elif command.startswith("End"):
        action, substring = command.split()
        if txt.endswith(substring):
            print("True")
        else:
            print("False")

    elif command.startswith("Uppercase"):
        txt = txt.upper()
        print(txt)

    elif command.startswith ("FindIndex"):
        action, ch = command.split()
        i = txt.find(ch)
        print(i)

    elif command.startswith("Cut"):
        action, begin_with_ch, count = command.split()
        begin_with_ch = int(begin_with_ch)
        count = int(count)
        cut_chars = txt[begin_with_ch:begin_with_ch + count]
        print(cut_chars)

