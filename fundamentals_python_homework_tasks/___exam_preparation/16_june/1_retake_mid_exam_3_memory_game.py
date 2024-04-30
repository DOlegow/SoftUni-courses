def play_memory_game():
    sequence = input().split()
    moves = 0

    while True:
        command = input()
        if command == "end":
            break

        moves += 1
        index_1, index_2 = map(int, command.split())

        if index_1 == index_2 or index_1 < 0 or index_1 >= len(sequence) or index_2 < 0 or index_2 >= len(sequence):
            new_elements = "-{}a".format(moves)
            mid_index = round(len(sequence)/2)
            sequence = sequence[:mid_index] + [new_elements] + [new_elements] + sequence[mid_index:]

            print("Invalid input! Adding additional elements to the board")
        elif sequence[index_1] == sequence[index_2]:
            element = sequence[index_1]
            del sequence[max(index_1, index_2)]
            del sequence[min(index_1, index_2)]

            print("Congrats! You have found matching elements - {}!".format(element))
        else:
            print("Try again!")

        if len(sequence) == 0:
            print("You have won in {} turns!".format(moves))
            return

    print("Sorry you lose :(")
    print(" ".join(sequence))

play_memory_game()
