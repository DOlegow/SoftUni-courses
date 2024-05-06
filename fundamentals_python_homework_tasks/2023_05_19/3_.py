import math
number_of_persons = int(input())
max_number_of_persons = int(input())
courses = math.ceil(number_of_persons/max_number_of_persons)
print(courses)
