n = int(input())
plant_dict = {}
plant = ''
rating = 0

for _ in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = plant_info[1]
    plant_dict[plant] = [rarity, []]

command = input()

while True:
    if command == "Exhibition":
        break

    action, i = command.split(": ")

    if action == 'Rate':
        plant_rating = i.split(" - ")
        plant = plant_rating[0]
        rating = float(plant_rating[1])
        if plant in plant_dict.keys():
            plant_dict[plant][1].append(rating)
        else:
            print('error')

    if action == 'Update':
        plant_new_rarity = i.split(" - ")
        new_rarity = plant_new_rarity[1]
        if plant_new_rarity[0] in plant_dict.keys():
            plant_dict[plant_new_rarity[0]][0] = new_rarity
        else:
            print('error')

    if action == 'Reset':
        del_rarity = i.split(" - ")
        if del_rarity[0] in plant_dict.keys():
            plant_dict[del_rarity[0]][1] = []
        else:
            print('error')

    command = input()

print("Plants for the exhibition:")
for plant_name, (rarity, ratings) in plant_dict.items():
    if len(ratings) > 0:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")

