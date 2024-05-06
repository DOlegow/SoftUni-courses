neighborhood = input().split('@')
neighborhood = [int(x) for x in neighborhood]

command = input()
current_house = 0

while True:
    if command == "Love!":
        break
    tokens = command.split(' ')
    step = int(tokens[1])

    if (current_house + step) >= len(neighborhood):
        current_house = 0
    else:
        current_house += step

    if neighborhood[current_house] == 0:
        print(f"Place {current_house} already had Valentine's day.")

    else:
        neighborhood[current_house] -= 2
        if neighborhood[current_house] == 0:
            print(f"Place {current_house} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_house}.")

if all(num == 0 for num in neighborhood):
    print("Mission was successful.")
else:
    house_count = [num for num in neighborhood if num != 0]
    print(f"Cupid has failed {len(house_count)} places.")
