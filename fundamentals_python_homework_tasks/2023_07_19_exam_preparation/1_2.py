def decrypting_message(message):
    while True:
        command = input()

        if command.startswith("Reveal"):
            print(f"You have a new text message: {message}")
            break

        current_command, *params = command.split(":|:")

        if current_command == "InsertSpace":
            index = int(params[0])
            message = message[:int(index)] + " " + message[int(index):]
            print(message)

        elif current_command == "Revers":
            substr = params[0]
            if substr in message:
                message = message.replace(substr, "", 1)
                message = message + substr[::-1]
                print(message)
            else:
                print("error")

        elif current_command == "ChangeAll":
            substring, replacement = params
            message = message.replace(substring, replacement)
            print(message)

data = input()
decrypting_message(data)