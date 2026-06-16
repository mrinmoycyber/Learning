# A generator is a function that uses the yield keyword to produce values one at a time instead of returning them all at once. 
# Generators are memory-efficient because they generate values lazily and maintain their execution state between calls to next(). 
# They are commonly used for processing large datasets, streaming data, and implementing custom iterators.

# Why Use Generators?
# Imagine numbers from 1 to 1,000,000.
# List Approach
# def get_numbers():
#     return list(range(1, 1000001))

# This creates all one million numbers in memory.

# Generator Approach
# def get_numbers():
#     for i in range(1, 1000001):
#         yield i
# Now only one number exists at a time.
# Memory usage is dramatically lower.

# A generator is a special type of function that produces values one at a time, instead of creating and returning all values at once.
# The key keyword is:
# yield
# instead of:
# return

#How yield Works
def count():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3


gen = count()

print(next(gen))

# Output:
# Start
# 1

# The function pauses at the yield.
# Next call:
# print(next(gen))
# Output:
# Middle
# 2

# The function resumes exactly where it stopped.

# Next call:
# print(next(gen))
# Output:
# End
# 3