# Find day month and year from date 'dd/mm/yy'
# split() method returns a list. This method splits a string into a list of substrings based on a specified delimiter. Each substring becomes an element in the resulting list.

mydate = input('Please enter the date dd/mm/yy')

a = mydate.split('/')

print('Day :', a[0])
print('Month :', a[1])
print('Year :', a[2])

# o/p - Please enter the date dd/mm/yy15/09/2024 
# Day : 15   
# Month : 09 
# Year : 2024