txt = input().upper()
current_string_of_ch = ''
rage_message = ''
non_digit_symbols = ''
number = ''
for i in range(len(txt)):
    if not txt[i].isdigit():
        current_string_of_ch += txt[i]
        non_digit_symbols += txt[i]
    else:
        for j in range(i, len(txt)):
            if not txt[j].isdigit():
                break
            number += txt[j]
        rage_message += current_string_of_ch * int(number)
        current_string_of_ch = ''
        number = ''
print(f'Unique symbols used: {(len(set(non_digit_symbols)))}')
print(rage_message)
