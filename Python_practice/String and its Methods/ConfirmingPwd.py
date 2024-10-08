pass1 = input('Enter Password')
pass2 = input('Confirm Password')

if pass1 == pass2:
    print('Yes they are matching')
else:
    if pass1.casefold() == pass2.casefold():
        print('Please check for the cases and try again')
    else:
        print('No they are not matching try again')
        
# casefold() is a method that returns a casefolded copy of the string, which is suitable for case-insensitive comparisons. 

# Use case 1 - Enter Password pass
#              Confirm Password pass
#              Yes they are matching  
# Use case 2 - Enter Passwordp asss
#              Confirm Password pas
#              No they are not matching try again
# Use case 3 - Enter Password pass
#              Confirm Password PaSs
#              Please check for the cases and try again