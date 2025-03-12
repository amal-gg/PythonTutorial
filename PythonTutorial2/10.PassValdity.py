s = input("Enter password: ")

has_lower = has_upper = has_digit = has_special = False

for ch in s:
    if 'a' <= ch <= 'z':
        has_lower = True
    elif 'A' <= ch <= 'Z':
        has_upper = True
    elif '0' <= ch <= '9':
        has_digit = True
    elif ch in "$#@":
        has_special = True

if len(s) >= 6 and has_lower and has_upper and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")
