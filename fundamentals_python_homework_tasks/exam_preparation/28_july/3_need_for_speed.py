def need_for_seed_III():
    cars = {}  # Dictionary to store car details {car_name: [mileage, fuel]}
    n = int(input())  # Number of cars

    for _ in range(n):
        car_info = input().split("|")
        car_name = car_info[0]
        mileage = int(car_info[1])
        fuel = int(car_info[2])
        cars[car_name] = [mileage, fuel]

    command = input()

    while command != "Stop":
        action, *args = command.split(" : ")

        if action == "Drive":
            car_name, distance, required_fuel = args
            distance, required_fuel = int(distance), int(required_fuel)

            if cars[car_name][1] < required_fuel:
                print("Not enough fuel to make that ride")
            else:
                cars[car_name][0] += distance
                cars[car_name][1] -= required_fuel
                print(f"{car_name} driven for {distance} kilometers. {required_fuel} liters of fuel consumed.")

                if cars[car_name][0] >= 100000:
                    del cars[car_name]
                    print(f"Time to sell the {car_name}!")

        elif action == "Refuel":
            car_name, fuel_to_add = args
            fuel_to_add = min(int(fuel_to_add), 75 - cars[car_name][1])

            cars[car_name][1] += fuel_to_add
            print(f"{car_name} refueled with {fuel_to_add} liters")

        elif action == "Revert":
            car_name, kilometers = args
            kilometers = int(kilometers)
            if cars[car_name][0] - kilometers < 10000:
                cars[car_name][0] = 10000
            else:
                cars[car_name][0] = cars[car_name][0] - kilometers
            if cars[car_name][0] > 10000:
                print(f"{car_name} mileage decreased by {kilometers} kilometers")

        command = input()

    for car, details in cars.items():
        print(f"{car} -> Mileage: {details[0]} kms, Fuel in the tank: {details[1]} lt.")


# Call the function to start the game
need_for_seed_III()

