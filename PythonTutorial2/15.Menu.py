def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

nCr = factorial(n) // (factorial(r) * factorial(n - r))

print(f"nCr ({n}C{r}) =", nCr)

