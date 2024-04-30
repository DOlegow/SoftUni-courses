def loot(chest, items):
    for item in items:
        if item not in chest:
            chest.insert(0, item)
    return chest

def drop(chest, index):
    if 0 <= index < len(chest):
        chest.append(chest.pop(index))
    return chest

def steal(chest, count):
    stolen_items = chest[-count:]
    chest = chest[:-count]
    return chest, stolen_items

def calculate_average_gain(chest):
    if not chest:
        print("Failed treasure hunt.")
    else:
        total_length = sum(len(item) for item in chest)
        average_gain = total_length / len(chest)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

treasure_chest = input().split("|")

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    elif command[0] == "Loot":
        items = command[1:]
        treasure_chest = loot(treasure_chest, items)
    elif command[0] == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif command[0] == "Steal":
        count = int(command[1])
        treasure_chest, stolen_items = steal(treasure_chest, count)
        print(", ".join(stolen_items))

calculate_average_gain(treasure_chest)