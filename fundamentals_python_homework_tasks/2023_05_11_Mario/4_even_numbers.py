n = int(input())
for i in range(n):
    flag = True
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        flag = False
        break
if flag:
    print('All numbers are even.')
