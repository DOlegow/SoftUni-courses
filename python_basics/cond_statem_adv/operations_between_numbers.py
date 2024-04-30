N1 = int(input())
N2 =  int(input())
operator = input()
rezult = 0

if operator == "+":
    rezult = N1 + N2
    if rezult % 2 == 0:
        print(f'{N1} {operator} {N2} = {rezult} - even')
    if rezult % 2 != 0:
        print(f'{N1} {operator} {N2} = {rezult} - odd')
elif operator== "-":
    rezult = N1-N2
    if rezult % 2 == 0:
        print(f'{N1} {operator} {N2} = {rezult} - even')
    if rezult % 2 != 0:
        print(f'{N1} {operator} {N2} = {rezult} - odd')
elif operator== "*":
    rezult = N1*N2
    if rezult % 2 == 0:
        print(f'{N1} {operator} {N2} = {rezult} - even')
    if rezult % 2 != 0:
        print(f'{N1} {operator} {N2} = {rezult} - odd')


if operator == "/":
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        rezult = N1 / N2
        print(f'{N1} / {N2} = {rezult:.2f}')

if operator == "%":
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        rezult = N1 % N2
        print(f'{N1} % {N2} = {rezult}')