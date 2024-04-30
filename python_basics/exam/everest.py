days = 0
high = 5364
count_days = 1
yes_no = ''
flag = False

while True:
    yes_no = input()
    if yes_no == "END":
        break
    elif yes_no == 'Yes':
        count_days += 1
        if count_days > 5:
            print('Failed!')
            print(f'{round(high)}')
            flag = True
            break
    if flag:
        break
    m = float(input())
    high += m
    if high >= 8848:
        break

if high >= 8848:
    print(f'Goal reached for {count_days} days!')
elif yes_no == "END":
    print('Failed!')
    print(f'{round(high)}')

