# Display data in  given format (25 letters)

# Product Name...........price
# Chicken Pizza..........300

item = input('Enter the item')
price = input('Enter price')

total_len = len(item) + len(price)
print(total_len)

dots = '.' * (25 - total_len)
print(item+dots+price)