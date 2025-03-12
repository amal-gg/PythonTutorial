s = input("Enter a string: ")

if " " in s:
    result = ""
    for ch in s:
        if ch == " ":
            result += "*"
        else:
            result += ch
else:
    result = "$" + s + "$"

print("Modified string:", result)
