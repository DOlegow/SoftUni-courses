n = int(input())
name = ''
new_name = ''
age = ''
c = 0
list_of_strings = []
for i in range(n):
    string = input()
    list_of_strings = string.split(' ')
    for el in list_of_strings:
        for ch in el:
            if ch == '@':
                name = el[1:]
                for l in name:
                    new_name += l

                    if l == '|':
                        new_name = new_name.replace(l, '')
                        break
                c += 1

            if ch.isdigit():
                age += str(ch)
    print(f'{new_name} is {age} years old.')
    new_name = ''
    age = ''

