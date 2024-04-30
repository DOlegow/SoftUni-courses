string_numbers = input().split()
integer_numbers = []
for element in string_numbers:
    number = int(element)
    integer_numbers.append(number)
sorted_numbers = sorted(integer_numbers)

print(sorted_numbers)

