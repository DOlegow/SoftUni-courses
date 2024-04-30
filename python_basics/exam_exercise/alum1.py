n = int(input())
size = input()
receiving = input()
price = 0

if n < 10:
    print('Invalid order')
elif n >= 10:
    if size == "90X130":
        price = 110
        if n > 60:
            price = n*(price - price * 0.08)
            if receiving == "With delivery":
                if n > 99:
                    price = (price + 60) - (price + 60) * 0.04
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
            elif receiving == "Without delivery":
                if n > 99:
                    price = price + 60
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
        elif n > 30:
            price = n*(price - price * 0.05)
            if receiving == "With delivery":
                if n > 99:
                    price = (price + 60) - (price + 60) * 0.04
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
            elif receiving == "Without delivery":
                if n > 99:
                    price = price + 60
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
    if size == "100X150":
        price = 140
        if n > 80:
            price = n*(price - price * 0.1)
            if receiving == "With delivery":
                if n > 99:
                    price = (price + 60) - (price + 60) * 0.04
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
            elif receiving == "Without delivery":
                if n > 99:
                    price = price + 60
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
        elif n > 40:
            price = n*(price - price * 0.06)
            if receiving == "With delivery":
                if n > 99:
                    price = (price + 60) - (price + 60) * 0.04
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
            elif receiving == "Without delivery":
                if n > 99:
                    price = price + 60
                    print(f'{price:.2f} BGN')
                elif n <= 99:
                    print(f'{price:.2f} BGN')
        if size == "130X180":
            price = 190
            if n > 50:
                price = n * (price - price * 0.12)
                if receiving == "With delivery":
                    if n > 99:
                        price = (price + 60) - (price + 60) * 0.04
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
                elif receiving == "Without delivery":
                    if n > 99:
                        price = price + 60
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
            elif n > 20:
                price = n * (price - price * 0.07)
                if receiving == "With delivery":
                    if n > 99:
                        price = (price + 60) - (price + 60) * 0.04
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
                elif receiving == "Without delivery":
                    if n > 99:
                        price = price + 60
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
        if size == "200X300":
            price = 250
            if n > 50:
                price = n * (price - price * 0.14)
                if receiving == "With delivery":
                    if n > 99:
                        price = (price + 60) - (price + 60) * 0.04
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
                elif receiving == "Without delivery":
                    if n > 99:
                        price = price + 60
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
            elif n > 25:
                price = n * (price - price * 0.09)
                if receiving == "With delivery":
                    if n > 99:
                        price = (price + 60) - (price + 60) * 0.04
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')
                elif receiving == "Without delivery":
                    if n > 99:
                        price = price + 60
                        print(f'{price:.2f} BGN')
                    elif n <= 99:
                        print(f'{price:.2f} BGN')