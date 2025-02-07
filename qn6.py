word = input("Enter a word: ")
if len(word) > 1:
    swapped_word = word[-1] + word[1:-1] + word[0]
else:
    swapped_word = word
print(f"Modified word: {swapped_word}")