numbers = input().split()
numbers = [int(num) for num in numbers]

average = sum(numbers) / len(numbers)
greater_numbers = [num for num in numbers if num > average]

top_numbers = sorted(greater_numbers, reverse=True)[:5]

if top_numbers:
    print(' '.join(map(str, top_numbers)))
else:
    print('No')
