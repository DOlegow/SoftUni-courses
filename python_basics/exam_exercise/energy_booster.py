fruit = str(input())
size = str(input())
number = int(input())
price = 0
price1 = 0

if size == "small":
    if fruit == "Watermelon":
        price1 = 56 * 2
    elif fruit == "Mango":
        price1 = 36.66 * 2
    elif fruit == "Pineapple":
        price1 = 42.1 * 2
    elif fruit == "Raspberry":
        price1 = 20 * 2
elif size == "big":
    if fruit == "Watermelon":
        price1 = 28.70 * 5
    elif fruit == "Mango":
        price1 = 19.60 * 5
    elif fruit == "Pineapple":
        price1 = 24.80 * 5
    elif fruit == "Raspberry":
        price1 = 15.20 * 5

price = number * price1
if price > 1000:
    price -= price * 0.5
elif 400 <= price <= 1000:
    price -= price * 0.15
elif price < 400:
    price = number * price1

print(f'{price:.2f} lv.')
