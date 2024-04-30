# read user input

month = str(input())
overnight_stay = int(input())
expences = 0
studio = 0
apartment = 0

# logic

if month == "May" or month == "October":
    studio = overnight_stay * 50
    if overnight_stay > 14:
        studio -= studio * 0.3
    elif overnight_stay > 7:
        studio -= studio*0.05
    apartment = overnight_stay * 65

if month == "June" or month == "September":
    studio = overnight_stay * 75.2
    if overnight_stay > 14:
        studio -= studio*0.2
    apartment = overnight_stay * 68.7

if month == "July" or month == "August":
    studio = overnight_stay * 76
    apartment = overnight_stay * 77

if overnight_stay > 14:
     apartment -= apartment*0.1

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')

