number_of_groups = int(input())
Musala = 0
MontBlanc = 0
Kilimanjaro = 0
k2 = 0
Everest = 0

for i in range(1, number_of_groups + 1):
    number_of_members = int(input())
    if number_of_members <= 5:
        Musala += number_of_members
    elif 6 <= number_of_members <= 12:
        MontBlanc += number_of_members
    elif 13 <= number_of_members <= 25:
        Kilimanjaro += number_of_members
    elif 26 <= number_of_members <= 40:
        k2 += number_of_members
    elif number_of_members >=41:
        Everest += number_of_members

total_people = Musala + MontBlanc + Kilimanjaro + k2 + Everest

percent_Musala = Musala / total_people * 100
percent_MontBlanc = MontBlanc / total_people * 100
percent_Kilimanjaro = Kilimanjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_Everest = Everest / total_people * 100

print(f'{percent_Musala:.2f}%')
print(f'{percent_MontBlanc:.2f}%')
print(f'{percent_Kilimanjaro:.2f}%')
print(f"{percent_k2:.2f}%")
print(f'{percent_Everest:.2f}%')

