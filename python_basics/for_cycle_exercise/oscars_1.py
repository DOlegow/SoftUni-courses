name = input()
points = float(input())
count_evaluative = int(input())
total_points = points

for i in range(1, count_evaluative+1):
    name_1 = input()
    point_1 = float(input())
    total_points += len(name_1) * point_1 / 2
    if total_points >= 1250.5:
        break



if total_points >= 1250.5:
    print(f'Congratulations, {name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {name} you need {(1250.5 - total_points):.1f} more!')