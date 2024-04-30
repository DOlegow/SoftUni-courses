list_of_products = input().split()
list_of_searched_products = input().split()
dict_products = {}
for i in range(0, len(list_of_products), 2):
    product = list_of_products[i]
    quantity = list_of_products[i + 1]
    dict_products[product] = int(quantity)
for searched in list_of_searched_products:
    if searched in dict_products:
        print(f"We have {dict_products[searched]} of {searched} left")
    else:
        print(f"Sorry, we don't have {searched}")
