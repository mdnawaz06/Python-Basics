import re

def is_valid_mobile_number(number):
    # Check if the number starts with 7,8 or 9
    if not re.match("^[789]", number):
        return False

    # Check if the number is 10 digits long
    if len(number) != 10:
        return False

    # Check if the number contains any non-numeric characters
    if not re.match("^[0-9]+$", number):
        return False

    return True
