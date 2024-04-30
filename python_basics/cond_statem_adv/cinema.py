# premiere = 12.00
# normal = 7.50
# discount = 5.00

type_projection = str(input())
lines = int(input())
columns = int(input())
income = 0

all_seats = lines * columns

if type_projection == "Premiere":
    income = all_seats * 12
elif type_projection == "Normal":
    income = all_seats * 7.5
elif type_projection == "Discount":
    income = all_seats * 5

print(f'{income:.2f} leva')