nilon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
price_nilon = (nilon+2)*1.5
price_paint = (paint+paint/100*10)*14.5
price_thinner = thinner*5
bags = 0.4
price_materials = price_nilon + price_paint + price_thinner + bags
salary_workers = price_materials/100*30*hours
all_expense = price_materials + salary_workers
print(f'Sum of all expense: {all_expense}')
