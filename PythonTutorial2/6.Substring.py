s = input("Enter a string: ")
sub = input("Enter substring to remove: ")
result = ""

i = 0
while i < len(s):
    if s[i:i+len(sub)] == sub:
        i += len(sub)  # Skip the substring
    else:
        result += s[i]
        i += 1

print("Modified string:", result)
