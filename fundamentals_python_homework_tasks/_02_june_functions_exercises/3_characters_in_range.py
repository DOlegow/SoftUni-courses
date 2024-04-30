def characters_in_range(char_one, char_two):
    character = []
    for i in range(ord(char_one) + 1, ord(char_two)):
        character.append(chr(i))
    return character


first_character = input()
second_character = input()
result = characters_in_range(first_character, second_character)
print(' '.join(result))