def smallest_of_three_numbers(number_one, number_two, number_three):
    if number_three > number_one < number_two:
        return number_one
    if number_one > number_two < number_three:
        return number_two
    else:
        return number_three


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_of_three_numbers(first_number, second_number, third_number))
