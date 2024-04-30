walk_min = int(input())
walk_number = int(input())
calorie = int(input())
total_cal_burned = 0

total_cal_burned = walk_number * walk_min * 5

if total_cal_burned >= (calorie * 0.5):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_cal_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_cal_burned}.')