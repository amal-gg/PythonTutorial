n = int(input("Enter number of elements: "))
total = 0

for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        total += num

print("Sum of even numbers:", total)
