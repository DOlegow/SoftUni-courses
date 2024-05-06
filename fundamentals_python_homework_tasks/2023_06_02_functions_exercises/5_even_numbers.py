def is_even(n):
    return n % 2 == 0


string_numbers = input().split()
numbers = []
for element in string_numbers:
    number = int(element)
    numbers.append(number)
even_numbers = list(filter(is_even, numbers))

print(even_numbers)
