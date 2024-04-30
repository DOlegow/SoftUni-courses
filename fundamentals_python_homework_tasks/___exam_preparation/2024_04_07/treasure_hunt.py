initial_loot = input().split('|')
command = input()
index = 0
stolen = []
averageGain = 0
Gain = 0
while command != "Yohoho!":
    if command.startswith('Loot'):
        items_list = command.split()
        for i in range(1,len(items_list)):
            if items_list[i] not in initial_loot:
                initial_loot.insert(0,items_list[i])
    elif command.startswith('Drop'):
        _,indx = command.split()
        if 0 <= int(indx) <= len(initial_loot):
            index = int(indx)
            item = initial_loot.pop(index)
            initial_loot.append(item)
    elif command.startswith('Steal'):
        _,count = command.split()
        count = int(count)
        if count < len(initial_loot):
            stolen = (initial_loot[count:])
            initial_loot = initial_loot[:-count]

    command = input ()
if len(initial_loot) == 0:
    print("Failed treasure hunt.")
for el in initial_loot:
    Gain += len(el)
averageGain = Gain / len(initial_loot)
print(', '.join(stolen))
print(f"Average treasure gain: {averageGain:.2f} pirate credits.")

