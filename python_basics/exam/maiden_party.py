party_price = float(input())
love_note = int(input())
roses = int(input())
keys_keeper = int(input())
caricatures = int(input())
luck = int(input())
remain = 0
needed = 0


sum = love_note * 0.6 + roses * 7.2 + keys_keeper * 3.6 + caricatures * 18.2 + luck * 22
count_art = love_note + roses + keys_keeper + caricatures + luck

if count_art > 25:
    sum -= sum * 0.35

host = sum * 0.1

profit = sum - host

if profit > party_price:
    remain = profit - party_price
    print(f'Yes! {remain:.2f} lv left.')

elif profit < party_price:
    needed = party_price - profit
    print(f'Not enough money! {needed:.2f} lv needed.')