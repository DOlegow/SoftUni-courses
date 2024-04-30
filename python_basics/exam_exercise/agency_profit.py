name = input()
number_ticket_adults = int(input())
number_ticket_child = int(input())
price_adults = float(input())
fee = float(input())
price_adult = 0
price_child = 0
total_price = 0
profit = 0

price_child = price_adults - price_adults * 0.7 + fee
price_adult = price_adults + fee
total_price = (price_child * number_ticket_child + price_adult * number_ticket_adults)
profit = total_price * 0.2

print(f'The profit of your agency from {name} tickets is {profit:.2f} lv.')