number = float(input())

if number == 0:
    print('zero')
elif number > 0:
    if abs(number) > 1000000:
        print('large positive')
    elif abs(number) < 1:
        print('small positive')
    else:
        print('positive')
elif number < 0:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')