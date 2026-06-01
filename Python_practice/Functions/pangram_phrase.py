#A pangram is a sentence that contains every letter of the English alphabet (a–z) at least once. 
# The quick brown fox jumps over the lazy dog

#removing special characters from the sen - re.sub(r'[^a-zA-Z]','',phrase)

import re

# def phrase(sen):
#     letters = re.sub(r'[^a-zA-Z]','',sen)
#     letter_set = set(letters.lower())
    
#     if len(letter_set) == 26:
#         return True
#     else:
#         return False
    
# sen = "The quick brown fox jumps over the lazy dog"
# print(phrase(sen))

def phrase(sen):
    letter_set = {ch.lower() for ch in sen if ch.isalpha()}
    return len(letter_set) == 26
sen = "The quick brown fox jumps over the lazy dog"
#sen = "Hello"
print(phrase(sen))

# def is_pangram(sentence):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     sentence = sentence.lower()

#     for letter in alphabet:
#         if letter not in sentence:
#             return False

#     return True

# print(is_pangram("The quick brown fox jumps over the lazy dog"))


# def is_pangram(sentence):
#     return len(set(sentence.lower()) & set("abcdefghijklmnopqrstuvwxyz")) == 26

# print(is_pangram("The quick brown fox jumps over the lazy dog"))
    

# isalpha() keeps only alphabetic characters.
# set() removes duplicates.
# If there are 26 unique letters, the sentence is a pangram. 

# def phrase(sen):
#     letter_set = {
#         ch.lower()
#         for ch in sen
#         if ch.isalpha()
#     }
#     return len(letter_set) == 26

# sen = "The quick brown fox jumps over the lazy dog"
# print(phrase(sen))