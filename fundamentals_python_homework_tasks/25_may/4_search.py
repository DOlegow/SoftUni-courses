n = int(input())
word = input()
list_of_strings = []

for i in range(n):
    string = input()
    list_of_strings.append(string)
print(list_of_strings)

for j in range(len(list_of_strings) - 1, -1, -1):
    el = list_of_strings[j]
    if word not in el:
        list_of_strings.remove(el)

print(list_of_strings)
