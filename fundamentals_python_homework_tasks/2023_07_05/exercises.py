bakery = {}
elements = input().split()
for element in range(0, len(elements), 2):
    bakery[elements[element]] = elements[element + 1]

print(bakery)



