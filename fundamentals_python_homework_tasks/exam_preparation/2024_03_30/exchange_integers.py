a = input()
b: str = input()
print(f'Before:')
print(f'a = {a}')
print(f'b = {b}')
c = b
b = a
a = c
print('After:')
print(f'a = {a}')
print(f'b = {b}')
