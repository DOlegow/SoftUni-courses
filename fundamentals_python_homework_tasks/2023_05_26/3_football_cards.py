team_a = ['A-' + str(s) for s in range(1, 12)]
team_b = ['B-' + str(s) for s in range(1, 12)]
flag = False
list_of_cards = input().split()
for player in list_of_cards:

    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        flag = True
        break

print(f'Team A - {len ( team_a )}; Team B - {len ( team_b )}')
if flag:
    print('Game was terminated')

