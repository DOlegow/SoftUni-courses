phonebook = {}

while True:
    name_number = input().split('-')
    if name_number[0].isdigit():
       break
    phonebook[name_number[0]] = name_number[1]
for i in range(int(name_number[0])):
    name = input()
    if name in phonebook.keys():
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f"Contact {name} does not exist.")
