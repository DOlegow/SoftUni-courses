initial_needed_experience = float(input())
count_of_battles = int(input())

count_current_battle = 0
needed_experience = 0
while True:
    if needed_experience >= initial_needed_experience or count_current_battle == count_of_battles:
        break
    experience_earned_per_battle = float(input())
    count_current_battle += 1
    needed_experience += experience_earned_per_battle
    if count_current_battle % 3 == 0:
        needed_experience += experience_earned_per_battle * 0.15
    if count_current_battle % 5 == 0:
        needed_experience -= experience_earned_per_battle * 0.1
    if count_current_battle % 15 == 0:
        needed_experience += experience_earned_per_battle * 0.05
if needed_experience >= initial_needed_experience:
    print(f"Player successfully collected his needed experience for {count_current_battle} battles.")
else:
    experience = needed_experience - initial_needed_experience
    print(f'Player was not able to collect the needed experience, {abs(experience):.2f} more needed.')
