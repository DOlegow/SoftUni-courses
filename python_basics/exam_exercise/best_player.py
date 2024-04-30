max_goals = -1
name = ''
goals = 0
best_player = ''

while True:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = name
    if goals >= 10:
        break
if goals > 0:
    print(f'{best_player} is the best player!')
if goals >= 3:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')

