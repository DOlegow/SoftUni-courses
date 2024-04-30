budget = int(input())
season = str(input())
count_fishermans = int(input())

expences = 0

if season == "Spring":
    expences = 3000
    if count_fishermans <= 6:
        expences -= expences*0.1
    elif 7 <= count_fishermans <= 11:
        expences -= expences*0.15
    elif count_fishermans >= 12:
        expences -= expences*0.25

if season == "Summer" or season == "Autumn":
    expences = 4200
    if count_fishermans <= 6:
        expences -= expences*0.1
    elif 7 <= count_fishermans <= 11:
        expences -= expences*0.15
    elif count_fishermans >= 12:
        expences -= expences*0.25

if season == "Winter":
    expences = 2600
    if count_fishermans <= 6:
        expences -= expences*0.1
    elif 6 < count_fishermans <= 11:
        expences -= expences*0.15
    elif count_fishermans >= 12:
        expences -= expences*0.25

if count_fishermans % 2 == 0 and season != "Autumn":
    expences -= expences*0.05

if budget - expences >= 0:
    print(f'Yes! You have {budget-expences:.2f} leva left.')
else:
    print(f'Not enough money! You need {expences-budget:.2f} leva.')
