import re
list_of_destinations = []
travel_points = 0
string = input()
pattern = r"/(\b[A-Z][A-Za-z]{2,})/|=(\b[A-Z][A-Za-z]{2,})="
matches = re.findall(pattern,string)

for match in matches:
    for el in match:
        if el:
            list_of_destinations.append(el)
            travel_points += len(el)
print('Destinations:',', '.join(list_of_destinations))

print(f"Travel Points: {travel_points}")


