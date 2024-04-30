txt = input()
lst = txt.split()
result_string = ''
for i in range(len(lst)):
    for j in range(len(lst[i])):
        result_string += lst[i]
print(result_string)
