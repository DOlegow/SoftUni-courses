floors = int(input())
flat_per_floor = int(input())

flat_number = 0
flat_name = ''

for floor_n in range(floors, 0, -1):
    for flat_n in range(flat_per_floor):

        flat_number = floor_n*10 + flat_n

        if floor_n == floors:
            flat_name = f'L{flat_number}'

        elif floor_n % 2 == 0:
            flat_name = f'O{flat_number}'

        elif floor_n % 2 != 0:
            flat_name = f'A{flat_number}'

        print(flat_name, end=' ')
    print()