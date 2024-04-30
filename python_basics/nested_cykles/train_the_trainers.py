people_assessment = int(input())

input_line = input()
sum_all_grades = 0
count_all_grades = 0
while input_line != "Finish":
    presentation = input_line

    sum_current_grades = 0
    for i in range(1, people_assessment + 1):
        current_grade = float(input())
        count_all_grades += 1
        sum_all_grades += current_grade

        sum_current_grades += current_grade

    avg_current_grade = sum_current_grades / people_assessment
    print(f"{presentation} - {avg_current_grade:.2f}.")

    input_line = input()

avg_result = sum_all_grades / count_all_grades
print(f"Student's final assessment is {avg_result:.2f}.")