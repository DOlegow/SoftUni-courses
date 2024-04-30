n = int(input())
if 1 <= n <= 100:
    for i in range(n+1):
        print(' ' * (n-i), end='')
        print('*' * i, end='')
        print('|', end='')
        print('*' * i, end='')
        print(' ' * (n-i))