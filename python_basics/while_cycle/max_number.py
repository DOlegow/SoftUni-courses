n = input()
big = -10000000000000


while n != "Stop":
    number = int(n)
    if number > big:
        big = number
    n = input()
print(big)
