n = int(input())
st = ''
string_length = 0
flag = True

for i in n:
    string_length = len(st)
    for j in range(string_length):
        if st[j] == ',' or st[j] == '.' or st[j] == '_':
            flag = False
            break
    if flag:
        print(f'{st} is pure.')
    else:
        print(f'{st} is not pure!')

