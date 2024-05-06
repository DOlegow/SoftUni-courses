initial_energy = int(input())
energy = initial_energy
command = input()
count = 0
flag = True
while True:
    if command == "End of battle":
        break

    distance = int(command)
    if energy >= distance:
        energy -= distance
        count += 1
        if count % 3 == 0:
            energy += count
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        flag = False
        break
    command = input()
if flag:
    print(f"Won battles: {count}. Energy left: {energy}")
