import re

input_text = input()

pair = []
mirror_pair = []
word_matches = []

pattern = r"@[A-Za-z]{3,}@@[A-Za-z]{3,}@|#[A-Za-z]{3,}##[A-Za-z]{3,}#"
matches = re.findall(pattern, input_text)

for match in matches:
    pattern = r"\w+"
    word_matches = re.findall(pattern,match)
    pair += word_matches
if not matches:
    print("No word pairs found!")
else:
    for word in range(0, len(pair), 2):
        second = (pair[word + 1])[::-1]
        first = pair[word]
        if second == first:
            mirror_pair.append(first)
            mirror_pair.append(pair[word + 1])

    print(f"{len(matches)} word pairs found!")

if len(mirror_pair) > 0:
    print("The mirror words are:")
else:
    print("No mirror words!")
for index in range(0, len(mirror_pair), 2):
    if index == len(mirror_pair) - 2:
        print(f"{mirror_pair[index]} <=> {mirror_pair[index + 1]}")
    else:
        print(f"{mirror_pair[index]} <=> {mirror_pair[index + 1]}", end=', ')


