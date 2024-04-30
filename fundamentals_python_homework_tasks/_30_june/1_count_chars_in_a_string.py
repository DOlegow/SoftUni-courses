text = [ch for ch in input() if ch != ' ']
dict_text = {}
for i in text:
    if i not in dict_text:
        dict_text[i] = 0
    dict_text[i] += 1
for j in dict_text.keys():
    print(f'{j} -> {dict_text[j]}')
