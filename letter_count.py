def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

word = input("Enter a word: ")
result = count_letters(word)
print("Letter count:")
for letter, count in result.items():
    print(f"{letter}: {count}")
