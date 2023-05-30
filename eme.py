def letter_count(word):
    letter_count={}
    for letter in word:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter]=1
    return letter_count

word=input("Enter a word of group of words: ")
result=letter_count(word)
result=str(result).replace("{","").replace("}","")
print(result)
# for letter, count in result.items():
#     print(letter,"=", count)
   
# An empty loop
# word=input("Enter words: ")
# word_only=''.join(e for e in word if e.isnumeric())
# print(word_only)

# for letter in word_only:
# 	pass
# print('Last Letter :', letter)
