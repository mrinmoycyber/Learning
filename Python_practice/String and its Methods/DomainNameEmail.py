# Find user id and domain name from email address

email_id = 'mrinmoy.kar23@gmail.com'

# Find the index of '@' symbol to separate user id and domain name
atrate = email_id.find('@')
print(atrate)

# Print user id by slicing the email address from the beginning to the index of '@' symbol
print('user id:', email_id[:atrate])
# Print domain name by slicing the email address from the index of '@' symbol + 1 to the end
print('domain name:', email_id[atrate+1:])

# Expected output:
# atrate: 13
# user id: mrinmoy.kar23
# domain name: gmail.com
