n1 = int(input())
n2 = int(input())

for i in range(n1, n2+1):
    str_n = str(i)
    sum1 = 0
    sum2 = 0
    for j in range(0, len(str_n)):
        digit = int(str_n[j])
        if j % 2 == 0:
            sum1 += digit
        else:
            sum2 += digit

    if sum1 == sum2:
        print(i, '', end='')
