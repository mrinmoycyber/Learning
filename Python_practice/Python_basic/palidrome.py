#A Santa at NASA"
# Step 1: Clean the string
# Remove spaces and ignore capitalization:

# Original: "A Santa at NASA"
# Cleaned: "asantaatnasa"

# Step 2: Compare with its reverse
# The reverse of "asantaatnasa" is "asantaatnasa".
# Since the cleaned string is the same as its reverse, it is a palindrome.

# char.isalnum(): This method returns True if the character is either a letter or a number, and False otherwise.

# List comprehension: We loop through each character in the sentence, check if it's alphanumeric using isalnum(), and convert it to lowercase. Only the valid alphanumeric characters are kept.

# ''.join(...): This concatenates the list of valid characters into a single string.


def is_palindrome(sentence):
    #convert the sentence to lowercase and keep only aplhanumeric  characters
    cleaned_sentence = " ".join(char.lower()for char in sentence if char.isalnum())
    
    #check if the cleaned sentence is equal to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]

print(is_palindrome("A Santa at NASA"))
    
