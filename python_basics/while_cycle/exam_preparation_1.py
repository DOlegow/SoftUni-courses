count_unsatisfactory_grades = int(input())
message = input()
average_grade = 0
sum_grades = 0
count_grades = 0
count_tasks = 0
task = ''
grade = 0
last_problem = ''
flag = True

count_bad_grades = 0

while message != "Enough":
    task = message
    grade = int(input())
    count_grades += 1
    count_tasks += 1
    sum_grades += grade
    if grade <= 4:
        count_bad_grades += 1
        if count_bad_grades == count_unsatisfactory_grades:
            flag = False
            print(f'You need a break, {count_unsatisfactory_grades} poor grades.')
            break
    message = input()
if flag:
    average_grade = sum_grades / count_grades
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {count_tasks}')
    print(f'Last problem: {task}')

