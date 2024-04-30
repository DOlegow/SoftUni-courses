initial_health = 100
initial_bitcoins = 0
underground_rooms = input().split('|')
best_room = 0

for i in range(len(underground_rooms)):
    room = underground_rooms[i].split()
    command = room[0]
    value = int(room[1])

    if command == "potion":
        if initial_health + value > 100:
            healed_amount = 100 - initial_health
            initial_health = 100
        else:
            healed_amount = value
            initial_health += value
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        initial_bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        initial_health -= value
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            best_room = i + 1
            break

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
else:
    print(f"Best room: {best_room}")
