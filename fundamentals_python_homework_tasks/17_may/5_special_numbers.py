n = int(input())
for num in range(1, n+1):
    sum_of_digits = 0
    string_of_number = str(num)
    for i in range(len(string_of_number)):
        sum_of_digits += int(string_of_number[i])
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
