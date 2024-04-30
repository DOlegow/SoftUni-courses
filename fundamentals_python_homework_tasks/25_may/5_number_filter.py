n = int(input())
command = ''
list_of_numbers = []

for _ in range(n):
    number = int(input())
    list_of_numbers.append(number)
command = input()
filtered_numbers = []
if command == 'even':
    for num in list_of_numbers:
        if num % 2 == 0:
            filtered_numbers.append( num )
elif command == 'odd':
    for num in list_of_numbers:
        if num % 2 != 0:
            filtered_numbers.append( num )
elif command == 'negative':
    for num in list_of_numbers:
        if num < 0:
            filtered_numbers.append( num )
elif command == 'positive':
    for num in list_of_numbers:
        if num >= 0:
            filtered_numbers.append( num )

print(filtered_numbers)