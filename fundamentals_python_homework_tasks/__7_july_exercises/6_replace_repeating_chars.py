txt = input()
str_without_repetition = txt[0]
for ch in range(len(txt)-1):
    if txt[ch] != txt[ch + 1]:
        str_without_repetition += txt[ch+1]
print(str_without_repetition)
