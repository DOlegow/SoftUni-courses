txt = input()
for ch in range(len(txt)):
    if txt[ch] == ':':
        print(txt[ch] + txt[ch+1])
