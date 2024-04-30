age = int(input())
price_washmashine = float(input())
toy_price = int(input())
sum_toys=0
money=0
sum_lili=0
brother_count = 0

for i in range(1,age+1):
    if i % 2 != 0:
        sum_toys += 1
    if i % 2 == 0:
        brother_count += 1
        money += 10
        sum_lili = sum_lili+money
total_sum = sum_toys*toy_price + sum_lili - brother_count
if total_sum-price_washmashine >=0:
    print(f'Yes! {(total_sum - price_washmashine):.2f}')
else:
    print(f'No! {price_washmashine-total_sum:.2f}')