s = input("Enter a string: ")
odd_chars = ""
even_chars = ""

for i in range(len(s)):
    if i % 2 == 0:
        even_chars += s[i]
    else:
        odd_chars += s[i]

print("Odd indices:", odd_chars)
print("Even indices:", even_chars)
