days = int(input())
food = float(input())
biscuits = 0
total_eaten_food = 0
total_dog_food = 0
total_cat_food = 0

for i in range(1, days+1):
    dog_food = float(input())
    cat_food = float(input())
    total_dog_food += dog_food
    total_cat_food += cat_food

    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1
total_eaten_food = total_dog_food + total_cat_food
percent_eaten_food = total_eaten_food * 100 / food
percent_total_god_food = total_dog_food * 100 / total_eaten_food
percent_total_cat_food = total_cat_food * 100 / total_eaten_food

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f'{percent_total_god_food:.2f}% eaten from the dog.')
print(f'{percent_total_cat_food:.2f}% eaten from the cat.')