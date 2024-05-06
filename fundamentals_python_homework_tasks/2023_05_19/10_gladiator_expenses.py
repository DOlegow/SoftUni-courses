lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
count_shield_breaks = 0

for i in range(1, lost_fight_count + 1):
    if i % 2 == 0:
        expenses += helmet_price
        if i % 3 == 0:
            expenses += shield_price
            count_shield_breaks += 1
            if count_shield_breaks % 2 == 0:
                expenses += armor_price
    if i % 3 == 0:
        expenses += sword_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
