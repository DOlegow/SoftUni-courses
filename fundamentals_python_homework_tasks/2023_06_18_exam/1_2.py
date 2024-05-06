needed_experience = float(input())
count_of_battles = int(input())
battle_experience = float(input())
total_experience

for i in range(num_battles):

    if (i + 1) % 15 == 0:
        battle_experience += battle_experience * 0.05
    if (i + 1) % 3 == 0:
        battle_experience += battle_experience * 0.15
    if (i + 1) % 5 == 0:
        battle_experience -= battle_experience * 0.10
    total_experience += battle_experience
    if total_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {i + 1} battles")
remaining_experience = needed_experience - total_experience
print(f"Player was not able to collect the needed experience, {remaining_experience:.2f} more needed")