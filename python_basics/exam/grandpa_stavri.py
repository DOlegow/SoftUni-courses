days = int(input())
sum_degrees = 0
sum_l = 0

for i in range(1, days+1):
    liter = float(input())
    degrees = float(input())
    sum_degrees += liter * degrees
    sum_l += liter
average_gegree = sum_degrees/sum_l

print(f'Liter: {sum_l:.2f}')
print(f'Degrees: {average_gegree:.2f}')

if average_gegree < 38:
    print('Not good, you should baking!')
elif 38 <= average_gegree <=42:
    print('Super!')
elif average_gegree > 42:
    print('Dilution with distilled water!')