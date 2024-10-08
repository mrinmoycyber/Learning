#Find the maximum and minimum in a tuple
#Given a tuple of integers, return both the maximum and minimum values.

def find_min_max(my_tup):
    return max(my_tup), min(my_tup)

my_tup = (3, 5, 6, 2, 12, 1)
max_val, min_val = find_min_max(my_tup)
print(f"Maximum: {max_val}, Minimum: {min_val}")


# Function Call:
# The function find_min_max(my_tup) is called with my_tup as its argument.
# Inside the function, it calculates the maximum and minimum values of the tuple my_tup using max(my_tup) and min(my_tup).

# Return Value:
# The function returns a tuple containing two elements: the maximum value and the minimum value.
# For example, if my_tup = (3, 5, 6, 2, 7, 1), the function will return (7, 1).

# Tuple Unpacking:
# The returned tuple (7, 1) is unpacked into the variables max_val and min_val.
# This means:
# max_val will hold the value 7
# min_val will hold the value 1