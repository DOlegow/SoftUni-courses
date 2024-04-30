n=int(input())
for row in range(1, n+1):
    print(' ' * (n-row), end='')
    print('* ' * row, end='')
    print(' ' * (n-row))
for row1 in range(n-1, 0, -1):
    print(' ' * (n-row1), end='')
    print('* ' * row1, end='')
    print(' ' * (n-row1))
