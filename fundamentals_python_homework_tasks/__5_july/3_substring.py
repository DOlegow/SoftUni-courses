first_s = input()
second_s = input()
while first_s in second_s:
    second_s = second_s.replace(first_s, '')
print(second_s)