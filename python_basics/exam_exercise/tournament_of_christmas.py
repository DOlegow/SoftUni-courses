days = int(input())
sport = ''
money = 0
day_money = 0
result = ''
game_win = 0
game_lose = 0
day_win = 0

for i in range(1, days+1):
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            day_money += 20
            game_win += 1
        elif result == "lose":
            game_lose += 1
        sport = input()
    if game_win > game_lose:
        day_win += 1
        day_money += day_money * 0.1
        money += day_money
    elif game_win < game_lose:
        money += day_money
    game_win = 0
    game_lose = 0
    day_money = 0

if day_win > days/2:
    money += money*0.2
    print(f'You won the tournament! Total raised money: {money:.2f}')
elif day_win < days/2:
    print(f'You lost the tournament! Total raised money: {money:.2f}')
