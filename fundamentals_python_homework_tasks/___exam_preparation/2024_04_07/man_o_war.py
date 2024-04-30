def fire(pirate_ship, index, damage):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] -= damage
        if pirate_ship[index] <= 0:
            pirate_ship.pop(index)
            print("You won! The enemy ship has sunken.")
    return pirate_ship

def defend(warship, start_index, end_index, damage):
    if 0 <= start_index < len(warship) and 0 <= end_index < len(warship):
        for i in range(start_index, end_index + 1):
            warship[i] -= damage
            if warship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                return []
    return warship

def repair(pirate_ship, index, health, max_health):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)
    return pirate_ship

def status(pirate_ship, max_health):
    count = sum(1 for section in pirate_ship if section < max_health * 0.2)
    print(f"{count} sections need repair.")

pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health = int(input())

while True:
    command = input().split()
    if command[0] == "Retire":
        break
    elif command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])
        warship_status = fire(warship_status, index, damage)
    elif command[0] == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        pirate_ship_status = defend(pirate_ship_status, start_index, end_index, damage)
    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        pirate_ship_status = repair(pirate_ship_status, index, health, max_health)
    elif command[0] == "Status":
        status(pirate_ship_status, max_health)

if pirate_ship_status and warship_status:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
