price = float(input())
kg = float(input())
days = int(input())
number_bags = int(input())
total_price = 0
fee = 0

if kg < 10:
    fee = price * 0.2
elif 10 <= kg <= 20:
    fee = price * 0.5
elif kg > 20:
    fee = price
if days > 30:
    fee += fee * 0.1
elif 7 <= days <= 30:
    fee += fee * 0.15
elif days < 7:
    fee += fee * 0.4

total_price = fee * number_bags
print(f'The total price of bags is: {total_price:.2f} lv.')