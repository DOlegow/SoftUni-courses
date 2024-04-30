n=int(input())
max_num=0
sum=0
diff=0

for i in range(0,n):
    num=int(input())
    if num>max_num:
        max_num=num
    sum = sum + num
diff=abs(sum-max_num)
if diff == max_num:
    print('Yes')
    print(f'Sum = {diff}')
else:
    print('No')
    print(f'Diff = {abs(diff-max_num)}')
