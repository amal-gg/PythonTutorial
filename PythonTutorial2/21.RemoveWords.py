
str = input("Enter string: ")
word = input("Enter word to remove: ")
print("Modified string:", " ".join(w for w in str.split() if w != word))
    