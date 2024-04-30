n = int(input())
counter = 1
flag = False

for row in range(1, n+1):
    for col in range(1, row+1):

        if counter > n:
            flag = True
            break
        print(counter, '', end='')
        counter += 1
    if flag:
        break
    print()