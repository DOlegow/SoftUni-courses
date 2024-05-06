txt = input()
encrypted_txt = ''
for ch in txt:
    encrypted_txt += chr(ord(ch)+3)
print(encrypted_txt)
