# iter() creates an iterator from an iterable.
# next() retrieves the next element from that iterator. 
# A for loop internally uses these two functions to iterate over collections. When the iterator is exhausted, Python raises StopIteration.

nums = [1,2,3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2 
print(next(it))  # 3

# iter() converts an iterable (list, tuple, string, dictionary, etc.) into an iterator.

# numbers = [10, 20, 30]
# it = iter(numbers)
# print(it)

# # next() retrieves the next element from an iterator.

# numbers = [10, 20, 30]
# it = iter(numbers)

# print(next(it)) # 10
# print(next(it)) # 20 
# print(next(it)) # 30