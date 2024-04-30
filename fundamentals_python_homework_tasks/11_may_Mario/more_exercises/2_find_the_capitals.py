single_string = input()
capital_indices = []
for index, symbol in enumerate(single_string):
    if ord(symbol) in range(65, 91):
        capital_indices.append(index)
print(capital_indices)


