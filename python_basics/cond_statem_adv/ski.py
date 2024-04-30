days = int(input())
room = input()
rating = input()
expenses = 0

if room == "room for one person":
    expenses = (days-1) * 18
elif room == "apartment":
    if days < 10:
        expenses = (days-1) * 25
        expenses -= expenses*0.3
    elif 10 <= days <= 15:
        expenses = (days - 1) * 25
        expenses -= expenses * 0.35
    elif days > 15:
        expenses = (days - 1) * 25
        expenses -= expenses * 0.5
elif room == "president apartment":
    if days < 10:
        expenses = (days-1) * 35
        expenses -= expenses*0.1
    elif 10 <= days <= 15:
        expenses = (days - 1) * 35
        expenses -= expenses * 0.15
    elif days > 15:
        expenses = (days - 1) * 35
        expenses -= expenses * 0.2
if rating == "positive":
    expenses += expenses*0.25
elif rating == "negative":
    expenses -= expenses*0.1

print(f'{expenses:.2f}')