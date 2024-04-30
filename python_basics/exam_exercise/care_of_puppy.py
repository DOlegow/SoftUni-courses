food = int(input())
word = input()
daily_food = 0
food_remain = 0
eaten_food = 0
food_needed = 0

while word != "Adopted":
    daily_food = int(word)
    eaten_food += daily_food
    word = input()
if eaten_food <= food * 1000:
    food_remain = food * 1000 - eaten_food
    print('')
    print(f'Food is enough! Leftovers: {food_remain} grams.')
else:
    food_needed = eaten_food - food * 1000
    print(f'Food is not enough. You need {food_needed} grams more.')
