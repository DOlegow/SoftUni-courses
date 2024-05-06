number_of_fillings = int(input())
capacity = 255

for i in range(number_of_fillings):
    liters_of_water = int(input())
    if capacity - liters_of_water >= 0:
        capacity -= liters_of_water
    else:
        print('Insufficient capacity!')
print(255 - capacity)
