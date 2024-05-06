txt = input().split()
number = 0
sum_of_numbers = 0
for el in txt:
    if el[0].isupper():
        sum_of_numbers += int(el[1:len(el)-1]) / (ord(el[0]) - 64)

    elif el[0].islower():
        sum_of_numbers += int(el[1:len(el)-1]) * (ord(el[0]) - 96)

    if el[-1].isupper():
        sum_of_numbers -= (ord(el[-1]) - 64)

    elif el[-1].islower():
        sum_of_numbers += (ord(el[-1]) - 96)


print(f'{sum_of_numbers:.2f}')
