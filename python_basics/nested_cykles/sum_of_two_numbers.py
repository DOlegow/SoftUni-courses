begin = int(input())
end = int(input())
magic_n = int(input())
count = 0
k = False
j = True
for i in range(begin, end+1):
    for j in range(begin, end+1):
        count += 1
        if i + j == magic_n:
            k = True
            print(f'Combination N:{count} ({i} + {j} = {magic_n})')
            break
    if k:
        break
if not k:
    print(f'{count} combinations - neither equals {magic_n}')
