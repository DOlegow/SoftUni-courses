# read user input

price_ecs = float(input())

number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

# logic

total = number_puzzles * 2.60
total += number_talking_dolls * 3
total += number_teddy_bears * 4.1
total += number_minions * 8.2
total += number_trucks * 2

number_toys = number_puzzles + number_talking_dolls + number_teddy_bears + number_minions + number_trucks
if number_toys >= 50:
    total -= total * 0.25
total -= total * 0.1


# Print output

if total >= price_ecs:
    print(f'Yes! {total - price_ecs:.2f} lv left.')
else:
    print(f'Not enough money! {price_ecs - total:.2f} lv needed.')
