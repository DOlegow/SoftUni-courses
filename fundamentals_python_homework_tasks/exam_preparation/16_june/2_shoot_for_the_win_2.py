def shoot_targets(targets):
    targets = list(map(int, targets.split()))
    shot_count = 0

    while True:
        command = input()
        if command == "End":
            break

        index = int(command)
        if index < 0 or index >= len(targets):
            continue

        if targets[index] == -1:
            continue

        current_target = targets[index]
        targets[index] = -1
        shot_count += 1

        for i in range(len(targets)):
            if targets[i] == -1:
                continue

            if targets[i] > current_target:
                targets[i] -= current_target
            elif targets[i] <= current_target:
                targets[i] += current_target

    print(f"Shot targets: {shot_count} -> {' '.join(map(str, targets))}")


sequence = input()
shoot_targets(sequence)
