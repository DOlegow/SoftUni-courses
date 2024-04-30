operator = input()
first_number = int(input())
second_number = int(input())


def solve(a, b, operator):
    if operator == 'multiply':
        rezult = a * b
    elif operator == 'divide':
        rezult = int(a/b)
    elif operator == 'add':
        rezult = a + b
    elif operator == 'subtract':
        rezult = a - b
    return rezult

print(solve(first_number,second_number,operator))
