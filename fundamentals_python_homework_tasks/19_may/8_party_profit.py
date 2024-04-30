group_size = int(input())
days = int(input())
earned_coins_per_day = 0
coins = 0
for current_day in range(1, days+1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    earned_coins_per_day += 50
    earned_coins_per_day -= 2 * group_size
    if current_day % 3 == 0:
        earned_coins_per_day -= 3 * group_size
    if current_day % 5 == 0:
        earned_coins_per_day += group_size * 20
        if current_day % 3 == 0:
            earned_coins_per_day -= group_size * 2
coins = int(earned_coins_per_day / group_size)
print(f"{group_size} companions received {coins} coins each.")
