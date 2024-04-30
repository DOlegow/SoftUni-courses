import re


def valid_destination_function(destinations_data):

    pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
    travel_points = 0
    valid_destinations = []
    result = re.finditer(pattern, destinations_data)

    for current_destination in result:
        valid_destinations.append(current_destination.group(2))
        travel_points += len(current_destination.group(2))

    print(f"Destinations: {', '.join(valid_destinations)}\nTravel Points: {travel_points}")


data = input()
valid_destination_function(data)
