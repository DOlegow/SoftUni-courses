import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus_points = int(input())

max_bonus_points = 0
students_attendances = 0

for student in range(number_of_students):
    count_of_attendance = int(input())
    bonus = count_of_attendance / number_of_lectures * (5 + additional_bonus_points)

    if bonus > max_bonus_points:
        max_bonus_points = bonus
        students_attendances = count_of_attendance

print(f"Max Bonus: {math.ceil(max_bonus_points)}.")
print(f"The student has attended {students_attendances} lectures.")
