list_of_strings = input().split()

list_of_numbers = []
for n in list_of_strings:
    number = float(n)
    list_of_numbers.append(number)
list_of_absolute_nimbers = []
for n in list_of_numbers:
    absolute_number = abs(n)
    list_of_absolute_nimbers.append(absolute_number)
print(list_of_absolute_nimbers)
