# Two variables a and b. Swap their values without using a temporary value.

a = 5
b = 10

#swaping using tuple packing and unpacking
# first packs the right hand side b,a becomes the tuple (10, 5). Now unpacks the tuple (10, 5) and assign the values to a and b on the left hand side. So a = 10 , b = 5.

a,b = b,a 
print(f"a: {a}, b:{b}")

# Packing: The right side (b, a) is packed into a tuple ((10, 5)).
# Unpacking: The left side (a, b) unpacks the tuple values and assigns them accordingly (a = 10, b = 5).