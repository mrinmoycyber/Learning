#find maximum numbers
# def max3(a,b,c):
#     num = max(a,b,c)
#     return num
    
# print(max3(7,25,9))

# o/p - 25

def max3(a,b,c):
    if a > b:
        return a
    
    if b > c:
        return b
    
    else:
        return c
    
print(max3(55, 35, 25))