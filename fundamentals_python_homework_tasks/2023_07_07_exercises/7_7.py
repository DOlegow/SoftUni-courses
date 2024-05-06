some_string = input()
final_string = ""
strength = 0
index = 0

while index < len(some_string):
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    elif some_string[index] == ">":
        final_string += some_string[index]
        if index + 1 < len(some_string):
            strength += int(some_string[index + 1])

    else:
        final_string += some_string[index]

    index += 1

print(final_string)
