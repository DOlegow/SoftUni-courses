employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())

students_per_hour = employee1_efficiency + employee2_efficiency + employee3_efficiency
hours_needed = 0

while students_count > 0:
    hours_needed += 1

    if hours_needed % 4 == 0:
        hours_needed += 1

    students_count -= students_per_hour

print(f"Time needed: {hours_needed}h.")
