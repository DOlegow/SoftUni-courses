import math
n = int(input())
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
n_other_color_balls = 0
points = 0

for i in range(1, n+1):
    color = input()
    if color == "red":
        points += 5
        red_balls += 1
    elif color == "orange":
        points += 10
        orange_balls +=1
    elif color == "yellow":
        points += 15
        yellow_balls +=1
    elif color == "white":
        points += 20
        white_balls += 1
    elif color == "black":
        points = math.floor(points / 2)
        black_balls += 1
    else:
        n_other_color_balls += 1

print(f'Total points: {points}')
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {n_other_color_balls}")
print(f"Divides from black balls: {black_balls}")