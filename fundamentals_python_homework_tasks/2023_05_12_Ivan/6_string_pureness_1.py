n = int(input())


for i in range(n):
    text = input()
    flag = True
    for j in text:
        if j == '.' or j == ',' or j == '_':
            flag = False
            break
    if flag:
        print(f'{text} is pure.')
    else:
        print(f'{text} is not pure!')
