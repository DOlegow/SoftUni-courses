list_with_opposite_numbers = input().split()
opposite_number = []
for element in list_with_opposite_numbers:
    current_number = -int(element)
    opposite_number.append(current_number)
print(opposite_number)