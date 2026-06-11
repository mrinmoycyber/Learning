#print unique numbers
def unq_num(numbers):
    seen = set()
    unique_numbers = []
    
    for i in numbers:
        if i not in seen:
            seen.add(i)
            unique_numbers.append(i)
    return unique_numbers

numbers = [5,6,7,5,8,6]
print(unq_num(numbers))

#o/p - [5,6,7,8]