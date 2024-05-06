divisor = int(input())
boundary = int(input())

for i in range(boundary, 0, -1):
    if i % divisor == 0 and i <= boundary and i > 0:
        print(i)
        break
