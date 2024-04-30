days = int(input())
place = input()
rating = input()

price = 0
total_price = 0

if place == "room for one person":
    price = 18
elif place == "apartment":
    price = 25
    if days < 10:
        price -= price * 0.3
    if 10 <= days <= 15:
        price -= price * 0.35
    if days > 15:
        price = price * 0.5
elif place == "president apartment":
    price = 35
    if days < 10:
        price -= price * 0.1
    if 10 <= days <= 15:
        price -= price * 0.15
    if days > 15:
        price -= price * 0.2

total_price = price * (days-1)

if rating == "positive":
    total_price = total_price + total_price * 0.25
    print(f'{total_price:.2f}')
elif rating == "negative":
    total_price = total_price - total_price * 0.1
    print(f'{total_price:.2f}')

