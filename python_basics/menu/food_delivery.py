price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegan_menu = 8.15
number_chicken = int(input())
number_fish = int(input())
number_vegan = int(input())
sum_chicken = number_chicken*price_chicken_menu
sum_fish = number_fish*price_fish_menu
sum_vegan = number_vegan*price_vegan_menu
sum_menu = sum_chicken + sum_fish + sum_vegan
price_dessert = sum_menu/100*20
price_delivery = 2.5
total_price = sum_menu + price_dessert + price_delivery
print(total_price)

