points = 0

while True:
    username = input()

    if username == "End":
        break

    for ch in username:
        if ch == 'a':
            points += 1
        elif ch == 'b':
            points += 2
        elif ch == 'c':
            points += 3

print(f'Total points is: {points}')