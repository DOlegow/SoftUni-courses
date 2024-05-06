list_of_groceries = input().split("!")

while True:
    commands = input()
    if commands == "Go Shopping!":
        break

    tokens = commands.split(' ')
    command = tokens[0]
    stock = tokens[1]

    if command == "Urgent":
        if stock not in list_of_groceries:
            list_of_groceries.insert(0, stock)

    elif command == "Unnecessary":
        if stock in list_of_groceries:
            list_of_groceries.remove(stock)

    elif command == "Correct":
        new_stock = tokens[2]
        if tokens[1] in list_of_groceries:
            index = list_of_groceries.index(tokens[1])
            list_of_groceries[index] = new_stock

    elif command == "Rearrange":
        if stock in list_of_groceries:
            list_of_groceries.remove(stock)
            list_of_groceries.append(stock)


print(", ".join(list_of_groceries))
