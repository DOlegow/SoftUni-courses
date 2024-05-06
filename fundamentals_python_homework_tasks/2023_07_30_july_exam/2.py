import re


def check_str_validity(input_string):
    pattern = r"^!(?P<command>[A-Z][a-z]+)!:\[(?P<content>[A-Za-z]+)\]$"
    match = re.match(pattern, input_string)
    if match:
        command = match.group('command')
        content = match.group('content')
        return len(command) >= 3 and len(content) >= 8
    return False


def translate(input_string):
    pattern = r"^!(?P<command>[A-Z][a-z]+)!:\[(?P<content>[A-Za-z]+)\]$"
    match = re.match(pattern, input_string)
    if match:
        content = match.group('content')
        translated = " ".join(str(ord(char)) for char in content)
        return f"{match.group('command')}: {translated}"
    return "The message is invalid"


def action(enter_strings):
    for i in enter_strings:
        i = i.strip()
        if check_str_validity(i):
            translated_string = translate(i)
            print(translated_string)
        else:
            print("The message is invalid")


n = int(input())

input_strings = [input() for ch in range(n)]
action(input_strings)
