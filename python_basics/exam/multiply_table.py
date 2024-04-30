n = int(input())

str_n = str(n)


digit_3 = int(str_n[2])
digit_2 = int(str_n[1])
digit_1 = int(str_n[0])
for j in range(1, digit_3+1):
    for k in range(1, digit_2+1):
        for l in range(1, digit_1+1):
            res = j*k*l
            print(f'{j} * {k} * {l} = {res};')

