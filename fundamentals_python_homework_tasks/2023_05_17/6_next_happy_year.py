year = int(input())
while True:
    year += 1
    year_string = str(year)
    set_value = set(year_string)
    if len(year_string) == len(set_value):
        print(year)
        break