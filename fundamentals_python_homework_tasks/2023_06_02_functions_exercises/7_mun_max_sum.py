def min_max_and_sum(minimum_number, maximum_number, sum_of_all_numbers):

    sequence_string = input().split()
    sequence_numbers = []

    for element in sequence_string:
        number = int(element)
        sequence_numbers.append(number)

    minimum_number = min(sequence_numbers)
    maximum_number = max(sequence_numbers)
    sum_of_all_numbers = sum(sequence_numbers)

    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {maximum_number}")
    print(f"The sum number is: {sum_of_all_numbers}")


minimum_number = 0
maximum_number = 0
sum_of_all_numbers = 0

min_max_and_sum(minimum_number, maximum_number, sum_of_all_numbers)


