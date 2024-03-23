#Palindrome - s1 = madam (reversing) s2 = madam

#Palindrome - level, deified, rotator.
# Checking a string is a palindrome
new_string = 'radar'

rev_string = new_string[::-1]

if new_string == rev_string:
    print('Palindrome')
else: 
    print('Not a Palindrome')
    
# Convert a given string to palindrom
name_string = 'Mrinmoy'

rev_string = name_string[::-1]
str_palindrome = name_string + rev_string
print('Palindrome- '+ str_palindrome)
    


    
    