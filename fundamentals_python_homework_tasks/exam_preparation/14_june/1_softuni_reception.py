first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())
time = 0
total_capacity_of_employees = first_employee + second_employee + third_employee

while number_of_students > 0:
    number_of_students -= total_capacity_of_employees
    time += 1
    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")
