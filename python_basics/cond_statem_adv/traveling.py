budget = float(input())
season = input()

destination = ""
type_of_holiday = ""
expences = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_holiday = "Camp"
        expences = budget * 0.3
    elif season == "winter":
        type_of_holiday = "Hotel"
        expences = budget * 0.7

if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expences = budget * 0.4
        type_of_holiday = "Camp"
    elif season == "winter":
        type_of_holiday = "Hotel"
        expences = budget * 0.8

if budget > 1000:
    destination = "Europe"
    type_of_holiday = "Hotel"
    expences = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{type_of_holiday} - {expences:.2f}')
