def is_palindrome(word):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_word = ''.join(c.lower() for c in word if c.isalpha())
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome!")
else:
    print(f"{string} is not a palindrome.")

# def is_palindrome(word):
#     word_only=''.join(c.lower() for c in word if c.isalpha())
#     print("The word:",word_only)
#     the_word=word_only
#     rev_word=the_word[::-1]
#     print("ORIG:",the_word,"REVERSED:",rev_word)
#     if the_word==rev_word:
#         return True
#     else:
#         return False




# word=input("Enter a string: ")
# print("result",is_palindrome(word))
