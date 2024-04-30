def odd_even_sum(number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for s in range(len(number)):
        digit = int(number[s])
        if digit % 2 == 0:
            sum_of_even_digits += digit
        else:
            sum_of_odd_digits += digit

    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")


single_number = input()
odd_even_sum(single_number)

