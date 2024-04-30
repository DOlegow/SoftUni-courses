def username_length_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def username_char_valid(name):
    for ch in name:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def username_is_valid(name):
    if username_length_valid(name) and username_char_valid(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)
