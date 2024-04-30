def password_validation(password):
    valid = True
    digit_count = sum(char.isdigit() for char in password)
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        valid = False
    if digit_count < 2:
        print("Password must have at least 2 digits")
        valid = False
    return valid


some_password = input()
password_is_valid = password_validation(some_password)
if password_is_valid:
    print('Password is valid')
