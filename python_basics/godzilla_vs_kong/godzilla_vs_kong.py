# read input data

budget = float(input())
walk_on = int(input())
wear_price = float(input())

# logic

decor_price = budget*0.1
total_wear_price = walk_on * wear_price
if walk_on > 150:
    total_wear_price -= total_wear_price*0.1
total_sum = decor_price + total_wear_price
sum_left = budget-total_sum

# output

if total_sum > budget:
    print("Not enough money!")
    print(f'Wingard needs {total_sum - budget:.2f} leva more.')
if total_sum <= budget:
    print("Action!")
    print(f'Wingard starts filming with {budget - total_sum:.2f} leva left.')


