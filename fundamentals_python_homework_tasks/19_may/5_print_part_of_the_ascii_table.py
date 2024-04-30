start_character = int(input())
end_character = int(input())

for character in range(start_character, end_character+1):
    print(chr(character), end=' ')
