sum_ = float(input())
gender = input()
age = int(input())
sport = input()
price = 0
money = 0

if gender == "m":
    if age <= 19:
        if sport == "Gym":
            price = 42 - 42*0.2
        elif sport == "Boxing":
            price = 41 - 41*0.2
        elif sport == "Yoga":
            price = 45 - 45*0.2
        elif sport == "Zumba":
            price = 34 - 34*0.2
        elif sport == "Dances":
            price = 51 - 51*0.2
        elif sport == "Pilates":
            price = 39 - 39*0.2
    elif age > 19:
        if sport == "Gym":
            price = 42
        elif sport == "Boxing":
            price = 41
        elif sport == "Yoga":
            price = 45
        elif sport == "Zumba":
            price = 34
        elif sport == "Dances":
            price = 51
        elif sport == "Pilates":
            price = 39
if gender == "f":
    if age <= 19:
        if sport == "Gym":
            price = 35 - 35 * 0.2
        elif sport == "Boxing":
            price = 37 - 37 * 0.2
        elif sport == "Yoga":
            price = 42 - 42 * 0.2
        elif sport == "Zumba":
            price = 31 - 31 * 0.2
        elif sport == "Dances":
            price = 53 - 53 * 0.2
        elif sport == "Pilates":
            price = 37 - 37 * 0.2
    elif age > 19:
        if sport == "Gym":
            price = 35
        elif sport == "Boxing":
            price = 37
        elif sport == "Yoga":
            price = 42
        elif sport == "Zumba":
            price = 31
        elif sport == "Dances":
            price = 53
        elif sport == "Pilates":
            price = 37
if price <= sum_:
    print(f'You purchased a 1 month pass for {sport}.')
elif price > sum_:
    money = price - sum_
    print(f"You don't have enough money! You need ${money:.2f} more.")