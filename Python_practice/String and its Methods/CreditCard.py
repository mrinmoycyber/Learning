# Display credit card number

# Card no - 4534 5678 9238 1124
# Display - **** **** **** 1124

card_number = '4534 5678 9238 1124'

# Find the index of the last four digits
index_number = card_number.index('1124')
print(index_number)

# Extract the last four digits from the card number
lastDigits = card_number[15::]
# Create a string of four asterisks for masking the first 12 digits
four_number = '*' * 4 + ''
# Create the display number by concatenating the masked digits with the last four digits
display_number = four_number * 3 + lastDigits

# Print the masked credit card number
print(display_number)

# o/p -15
# ************1124
