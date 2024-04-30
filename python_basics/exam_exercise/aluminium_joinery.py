number = int(input())
kind = input()
received = input()
total_price = 0
price = 0

if number < 10:
    print("Invalid order")
else:
    if kind == "90X130":
        price = 110
        if number > 60:
            price -= price*0.08
        elif number > 30:
            price -= price*0.05

    elif kind == "100X150":
        price = 140
        if number > 80:
            price -= price*0.1
        elif number > 40:
            price -= price*0.06

    elif kind == "130X180":
        price = 190
        if number > 50:
            price -= price*0.12
        elif number > 20:
            price -= price*0.7

    elif kind == "200X300":
        price = 250
        if number > 50:
            price -= price*0.14
        elif number > 25:
            price -= price*0.09

    total_price = number * price

    if received == "With delivery":
        if number > 99:
            total_price += 60
            total_price -= total_price * 0.04
        elif number <= 99:
            total_price += 60
        print(f'{total_price:.2f} BGN')
    elif received == "Without delivery":
        if number > 99:
            total_price -= total_price * 0.4
        elif number <= 99:
            print(f'{total_price:.2f} BGN')


