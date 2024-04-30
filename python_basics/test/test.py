number = int(input())

is_valid = 100 <= number <= 200 or number == 0

if is_valid == False:
    print('invalid')

