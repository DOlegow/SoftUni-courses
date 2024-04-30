single_string = input()
digits = ''
letters = ''
others = ''
for character in single_string:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        others += character
print(digits)
print(letters)
print(others)
