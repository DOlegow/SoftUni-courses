n = input()
min_num = 10000000000000

while n != "Stop":
    mn = int(n)
    if mn < min_num:
        min_num = mn
    n = input()
print(min_num)
