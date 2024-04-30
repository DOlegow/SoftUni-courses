n = int(input())

def first_last_lines():
    print('+', end='')
    for i in range(n-2):
        print(' -', end='')
    print(' +')

def middle_lines():
    for row in range(n-2):
        print('|', end='')
        for col in range(n-2):
            print(' -', end='')
        print(' |')

def all_lines():
    first_last_lines()
    middle_lines()
    first_last_lines()

all_lines()
