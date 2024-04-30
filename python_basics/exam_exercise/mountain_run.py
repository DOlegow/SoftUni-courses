record = float(input())
distance = float(input())
time = float(input())
import math

time_all_distance = distance * time
delay = math.floor(distance / 50)
all_delay = delay * 30
total = time_all_distance + all_delay

if record <= total:
    print(f'No! He was {(total - record):.2f} seconds slower.')
else:
    print(f'Yes! The new record is {total:.2f} seconds.')