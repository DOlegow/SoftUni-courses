def add_gold(town, amount):
    global towns
    towns[town]['gold'] += amount
    print(f"{amount} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")

def prosper(town, amount):
    global towns
    towns[town]['gold'] += amount
    print(f"{town} now has {towns[town]['gold']} gold.")

def plunder(town, people, gold):
    global towns
    towns[town]['gold'] -= gold
    towns[town]['population'] -= people
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

def wipe_out(town):
    global towns
    del towns[town]
    print(f"{town} has been wiped off the map!")

def print_settlements():
    global towns
    for town, data in towns.items():
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")

towns = {}

while True:
    command = input().strip()
    if command == "Sail":
        break
    name, population, gold = command.split("||")
    towns[name] = {'population': int(population), 'gold': int(gold)}

while True:
    action = input().strip()
    if action == "End":
        break
    action_type, params = action.split("=>")[0], action.split("=>")[1:]
    if action_type == "Prosper":
        town, amount = params
        prosper(town, int(amount))
    elif action_type == "Plunder":
        town, people, gold = params
        plunder(town, int(people), int(gold))
    elif action_type == "Explosion":
        town = params[0]
        wipe_out(town)

print("Ahoy, Captain! All targets have been plundered and destroyed!" if not towns else f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
print_settlements()
