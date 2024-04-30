# read input
import math
world_record = float(input())
distance = float(input())
time_1m = float(input())

# logic
time_ivan = distance * time_1m
delay = distance/15
delay = math.floor(delay)
delay = delay*12.5
time_ivan += delay
if time_ivan < world_record:
    print(f'Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {(time_ivan - world_record):.2f} seconds slower.')