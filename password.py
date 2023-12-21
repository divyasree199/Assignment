import re

def is_valid_password(password):

    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_@$]).{8,}$')

    if re.match(pattern, password):
        return True
    else:
        return False

if __name__ == "__main__":
    password = input("Enter a password: ")

    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is not valid. Please ensure it meets the criteria.")
