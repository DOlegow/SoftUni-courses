text_reverse = ""
    while True:
        command = input()
        if command == "end":
            break
        text_reverse = ""
        for x in reversed(command):
            text_reverse += x
        print(f"{command} = {text_reverse}")
