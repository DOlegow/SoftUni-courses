import re
spent = 0
furniture = ''
text = input()
list_furnitures = []
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
while text != "Purchase":
    matches = re.search(pattern,text)

    if matches:
        furniture, price, quantity = matches.groups()
        money = float(price) * int(quantity)
        spent += money
        list_furnitures.append(furniture)
    text = input()
print('Bought furniture:')
for el in list_furnitures:
    print(el)
print(f"Total money spend: {spent:.2f}")