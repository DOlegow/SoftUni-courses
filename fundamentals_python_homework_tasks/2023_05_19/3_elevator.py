import math

number_of_persons = int(input())
max_number_of_persons = int(input())
courses = number_of_persons // max_number_of_persons
if number_of_persons > max_number_of_persons and number_of_persons % max_number_of_persons == 0:
    print(courses)
elif number_of_persons > max_number_of_persons and number_of_persons % max_number_of_persons != 0:
    print(courses + 1)
elif number_of_persons < max_number_of_persons:
    print(1)

