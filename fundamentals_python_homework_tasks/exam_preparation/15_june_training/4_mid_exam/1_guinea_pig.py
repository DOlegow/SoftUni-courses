quantity_of_food = float(input())
quantity_of_hay = float(input())
quantity_of_cover = float(input())
guinea_pig_weight = float(input())

for day in range(1, 31):
    quantity_of_food -= 0.3
    if day % 2 == 0:
        quantity_of_hay -= 0.05 * quantity_of_food
    if day % 3 == 0:
        quantity_of_cover -= guinea_pig_weight / 3
    if quantity_of_food <= 0 or quantity_of_hay <= 0 or quantity_of_cover <= 0:
        break

if quantity_of_food > 0 and quantity_of_hay > 0 and quantity_of_cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food:.2f}, Hay: {quantity_of_hay:.2f}, Cover: {quantity_of_cover:.2f}.")
else:
    print("Merry must go to the pet store!")
