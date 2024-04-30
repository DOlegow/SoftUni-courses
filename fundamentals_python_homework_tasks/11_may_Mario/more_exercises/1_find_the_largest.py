number = input()
largest_number = []
for digit in number:
    largest_number.append(digit)
sorted_largest_number = sorted(largest_number)
sorted_largest_number.reverse()
biggest_number = ''.join(sorted_largest_number)
print(biggest_number)
