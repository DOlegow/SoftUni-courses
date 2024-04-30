n = input()
min = 10000000000

while n != "Stop":
    num = int(n)
    if num < min:
        min = num
        n = input()
print(max)
