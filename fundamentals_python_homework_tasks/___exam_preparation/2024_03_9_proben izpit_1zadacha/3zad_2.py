def prosper(town, amount):
    global towns
    towns[town]['gold'] += amount
    print(f"{amount} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")

def plunder(town, people, gold):
    global towns
    towns[town]['gold'] -= gold
    towns[town]['population'] -= people
    if towns[town]['population'] <= 0 or towns[town]['gold'] <= 0:
        del towns[town]
        print ( f"{town} plundered! {gold} gold stolen, {people} citizens killed." )
        print(f"{town} has been wiped off the map!")
    else:
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

towns = {}

while True:
    command = input().strip()
    if command == "Sail":
        break
    name, population, gold = command.split("||")
    if name in towns:
        towns[name]['population'] += int(population)
        towns[name]['gold'] += int(gold)
    else:
        towns[name] = {'population': int(population), 'gold': int(gold)}

while True:
    action = input().strip()
    if action == "End":
        break
    action_type, params = action.split("=>")[0], action.split("=>")[1:]
    if action_type == "Prosper":
        town, amount = params
        if int(amount) < 0:
            print("Gold added cannot be a negative number!")
        else:
            prosper(town, int(amount))
    elif action_type == "Plunder":
        town, people, gold = params
        plunder(town, int(people), int(gold))

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town, data in towns.items():
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
