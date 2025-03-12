
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in "aeiouAEIOU":  
        result += ch  

print("String after removing vowels:", result)

    