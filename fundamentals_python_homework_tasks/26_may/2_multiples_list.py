factor = int(input())
count = int(input())

multiples_list = []
for i in range(1, count + 1):
    current_element = i * factor
    multiples_list.append(current_element)

print(multiples_list)