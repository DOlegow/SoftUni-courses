list_strings = input().split()
list_of_numbers = []
for n in list_strings:
    number = float(n)
    round_number = round(number)
    list_of_numbers.append(round_number)
print(list_of_numbers)
