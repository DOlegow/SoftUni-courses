def fill_lift():
    people_waiting = int(input())
    lift_state = list(map(int, input().split()))
    max_capacity = 4
    total_capacity = len(lift_state) * max_capacity
    current_fill = sum(lift_state)
    for i in range(len(lift_state)):
        while lift_state[i] < max_capacity:
            if people_waiting == 0:
                break
            current_fill += 1
            lift_state[i] += 1
            people_waiting -= 1

    if people_waiting == 0 and current_fill < len(lift_state) * max_capacity:
        print("The lift has empty spots!")
        print(" ".join(map(str, lift_state)))
    elif people_waiting > 0 and total_capacity == len(lift_state) * max_capacity:
        print("There isn't enough space! {} people in a queue!".format(people_waiting))
        print(" ".join(map(str, lift_state)))
    else:
        print(" ".join(map(str, lift_state)))


fill_lift()

