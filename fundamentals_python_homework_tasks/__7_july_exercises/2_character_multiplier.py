two_strings = input().split()
first_string = two_strings[0]
second_string = two_strings[1]
total_sum = 0
if len(first_string) > len(second_string):
    for ch in range(len(second_string)):
        total_sum += ord(first_string[ch]) * ord(second_string[ch])
    for ch in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[ch])
elif len(second_string) > len(first_string):
    for ch in range(len(first_string)):
        total_sum += ord(first_string[ch]) * ord(second_string[ch])
    for ch in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[ch])
else:
    for ch in range(len(first_string)):
        total_sum += ord(first_string[ch]) * ord(second_string[ch])
print(total_sum)
