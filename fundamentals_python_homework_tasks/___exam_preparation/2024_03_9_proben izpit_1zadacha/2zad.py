import re

def is_valid_emoji(emoji):
    if emoji.startswith("::") and emoji.endswith("::") and len(emoji.strip()) >= 3:
        emoji = emoji[2:-2]
        if emoji[0].isupper() and emoji[1:].islower():
            return True
    elif emoji.startswith("**") and emoji.endswith("**") and len(emoji.strip()) >= 5:
        emoji = emoji[2:-2]
        if emoji[0].isupper() and emoji[1:].islower():
            return True
    return False

def calculate_coolness(emoji):
    return sum(ord(char) for char in emoji if char.isalpha())

def extract_emojis(text):
    emojis = re.findall(r'[*]{2}[A-Z]{1}[a-z]{2,}[*]{2}|[:]{2}[A-Z]{1}[a-z]{2,}[:]{2}', text)
    return emojis


text = input()
cool_threshold = 1
for char in text:
    if char.isdigit():
        cool_threshold *= int(char)


print(f"Cool threshold: {cool_threshold}")


emojis = extract_emojis(text)
cool_emojis = []
for emoji in emojis:
    if is_valid_emoji(emoji):
        coolness = calculate_coolness(emoji)
        if coolness > cool_threshold:
            cool_emojis.append((emoji, coolness))


print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji, coolness in cool_emojis:
    print(f"{emoji}")
