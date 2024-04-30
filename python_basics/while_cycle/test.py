name = input()
grades = 1.0
sum_grades = 0.00
excluded = 0
flag = True
while grades <= 12:
    grade = float(input())
    if grade < 4:
        excluded += 1
        if excluded > 1:
            print(f'{name} has been excluded at {grades} grade')
            flag = False
            break

    else:
        sum_grades += grade
        grades += 1
    continue
if flag:
    average = sum_grades / 12
    print(f'{name} graduated. Average grade: {average:.2f}')




