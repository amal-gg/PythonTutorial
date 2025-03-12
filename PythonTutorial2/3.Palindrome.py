s = input("Enter a string: ")
reverse_s = ""

for ch in s:
    reverse_s = ch + reverse_s  

if s == reverse_s:
    print("Palindrome")
else:
    print("Not a palindrome")
