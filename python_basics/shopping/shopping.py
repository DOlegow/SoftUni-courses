# read user input
budget = float(input())
video = int(input())
CPU = int(input())
RAM = int(input())

price_video = 250

# logic
sum_video = video * price_video
total_sum = sum_video
total_sum += CPU * sum_video*0.35
total_sum += RAM * sum_video*0.1

if video > CPU:
    total_sum -= total_sum*0.15

# output
if (budget - total_sum) >= 0:
    print(f'You have {(budget - total_sum):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_sum - budget):.2f} leva more!')