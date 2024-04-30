numbers = input().split()
list_of_int_numbers = list(map(int, numbers))
n = int(input())
for i in range(n):
    min_number = min(list_of_int_numbers)
    list_of_int_numbers.remove(min_number)

string_list = map(str, list_of_int_numbers)
string_numbers = ', '.join(string_list)
print(string_numbers)
