import re

""" test_password = 'ASDfasg!12345' """

"""variant 1"""


def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%$*^!]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password...")
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols...")
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least 1 lowercase letter...")
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least 1 uppercase letter...")
    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least 1 number...")
    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least 1 special symbol (@%$*^!)...")
    return (True, "Password is valid!")


"""variant 2"""
"""
def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"[a-z]+")
    uppercase_pattern = re.compile(r"[A-Z]+")
    number_pattern = re.compile(r"[0-9]+")
    special_symbol_pattern = re.compile(r"[@%$*^!]+")

    errors = []

    if not re.fullmatch(length_pattern, password):
        errors.append("Password must have at least 8 symbols...")
    if not re.fullmatch(lowercase_pattern, password):
        errors.append("Password must have at least 1 lowercase letter...")
    if not re.fullmatch(uppercase_pattern, password):
        errors.append("Password must have at least 1 uppercase letter...")
    if not re.fullmatch(number_pattern, password):
        errors.append("Password must have at least 1 number...")
    if not re.fullmatch(special_symbol_pattern, password):
        errors.append("Password must have at least 1 special symbol (@%$*^!)...")

    if errors:
        return (False, errors)
    else:
        return (True, "Password meets all criteria.")
"""
""" print(check_password(test_password))  """


while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])
