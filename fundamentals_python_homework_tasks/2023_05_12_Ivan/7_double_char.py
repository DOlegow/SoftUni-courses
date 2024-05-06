symbols = input()
while symbols != "End":
    if symbols == "SoftUni":
        symbols = input()
        continue
    for i in range(len(symbols)):
        print(symbols[i]*2, end='')
    print()
    symbols = input()


