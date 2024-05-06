number_of_letters = int(input())
end_of_loop = 97 + number_of_letters

for i in range(97, end_of_loop):
    for j in range(97, end_of_loop):
        for k in range(97, end_of_loop):
            print(f'{chr(i)}{chr(j)}{chr(k)}')
