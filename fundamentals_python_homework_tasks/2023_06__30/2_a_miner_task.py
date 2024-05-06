string_list = []
string_dict = {}
sequence_of_strings = ''
while True:
    sequence_of_strings = input()
    if sequence_of_strings == 'stop':
        break
    string_list.append(sequence_of_strings)

for index in range(0, len(string_list), 2):
    if string_list[index] not in string_dict.keys():
        string_dict[string_list[index]] = 0
    string_dict[string_list[index]] += int(string_list[index + 1])
for key, value in string_dict.items():
    print(f'{key} -> {value}')

