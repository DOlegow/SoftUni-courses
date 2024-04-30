n = int(input())
bonus = 0

if n > 1000:
    bonus += n*0.1
elif n > 100:
    bonus += n * 0.2
elif n <= 100:
    bonus += 5
if n % 2 == 0:
     bonus += 1
if n % 10 == 5:
     bonus += 2
print(bonus)
print(bonus + n)
