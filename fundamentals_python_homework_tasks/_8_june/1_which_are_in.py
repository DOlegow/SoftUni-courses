first_sequence = input().split(', ')
second_sequence = input().split(', ')

which_are_in = [x for x in first_sequence if any(x in element for element in second_sequence)]

print(which_are_in)
