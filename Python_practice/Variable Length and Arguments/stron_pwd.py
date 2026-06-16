# isalnum() is built-in python string method
# The name comes from:
# al = alphabetic characters (a-z, A-Z)
# num = numeric characters (0-9)

# It checks whether all characters in a string are letters or digits.
# string.isalnum()
# It returns:
# True → if the string contains only letters and/or digits
# False → if it contains spaces, special characters, or is empty

def is_strong_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if (
        len(password) >= 8
        and has_lower
        and has_upper
        and has_digit
        and has_special
    ):
        return True

    return False

print(is_strong_password("hello123"))      # False (no uppercase, no special)
print(is_strong_password("HELLO123"))      # False (no lowercase, no special)
print(is_strong_password("Hello123"))      # False (no special)
print(is_strong_password("Hello@"))        # False (length < 8 and no digit)
print(is_strong_password("Hello@123"))     # True