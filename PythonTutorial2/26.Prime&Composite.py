
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number of elements: "))
nums = []

for _ in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

primes = []
composites = []

for num in nums:
    if is_prime(num):
        primes.append(num)
    else:
        composites.append(num)

print("Primes:", primes)
print("Composites:", composites)

    