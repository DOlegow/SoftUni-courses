sequence = list(map(int, input().split()))

shot_targets = 0

while True:
    command = input()
    if command == "End":
        break

    ind = int(command)

    if ind < 0 or ind >= len(sequence):
        continue

    if sequence[ind] == -1:
        continue

    sequence[ind] = -1
    shot_targets += 1

    for i in range(len(sequence)):
        if sequence[i] == -1:
            continue

        if sequence[i] > sequence[ind]:
            sequence[i] -= sequence[ind]
        elif sequence[i] <= sequence[ind]:
            sequence[i] += sequence[ind]

print(f"Shot targets: {shot_targets} -> {' '.join(map(str, sequence))}")
