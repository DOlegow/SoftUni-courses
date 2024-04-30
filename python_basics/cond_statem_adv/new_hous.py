kind_of_flower = str(input())
count_of_flower = int(input())
budget = int(input())
expences = 0

if kind_of_flower == "Roses":
    expences = count_of_flower*5
    if count_of_flower > 80:
        expences -= expences*0.1

if kind_of_flower == "Dahlias":
    expences = count_of_flower*3.8
    if count_of_flower > 90:
        expences -= expences*0.15

if kind_of_flower == "Tulips":
    expences = count_of_flower*2.8
    if count_of_flower > 80:
        expences -= expences*0.15

if kind_of_flower == "Narcissus":
    expences = count_of_flower*3
    if count_of_flower < 120:
        expences += expences*0.15

if kind_of_flower == "Gladiolus":
    expences = count_of_flower*2.5
    if count_of_flower < 80:
        expences += expences*0.2

if budget >= expences:
    print(f'Hey, you have a great garden with {count_of_flower} {kind_of_flower} and {budget-expences:.2f} leva left.')
else:
    print(f'Not enough money, you need {expences-budget:.2f} leva more.')