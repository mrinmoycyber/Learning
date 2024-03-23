# Sorting Letters of a String

old_alpha = "zkhhsficdba"

# "Sorting the characters of the string will result in a list."
storing_str = sorted(old_alpha)
print(storing_str)
# Output: ['a', 'b', 'c', 'd', 'f', 'h', 'h', 'i', 'k', 's', 'z']

# Now it will return a string.
new_alpha = ''.join(storing_str)
print(new_alpha)
# o/p- abcdfhhiksz