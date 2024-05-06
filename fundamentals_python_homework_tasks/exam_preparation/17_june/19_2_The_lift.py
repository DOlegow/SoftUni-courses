waiting_people = int(input())
wagons_current_state = input()

list_of_wagons = list(map(int, wagons_current_state.split()))

for wagon in range(len(list_of_wagons)):
    for people_in_wagon in range(4):

        if list_of_wagons[wagon] < 4:

            if waiting_people > 0:
                waiting_people -= 1
                list_of_wagons[wagon] += 1
            else:
                break

if waiting_people == 0 and list_of_wagons.count(4) < len(list_of_wagons):
    print(f"The lift has empty spots!\n\
{' '.join(map(str, list_of_wagons))}")

elif waiting_people > 0 and list_of_wagons.count(4) == len(list_of_wagons):
    print(f"There isn't enough space! {waiting_people} people in a queue!\n{' '.join(map(str, list_of_wagons))}")

elif waiting_people == 0 and list_of_wagons.count(4) == len(list_of_wagons):
    print(f"{' '.join(map(str, list_of_wagons))}")

