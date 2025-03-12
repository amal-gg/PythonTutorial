n = int(input("Enter number of elements: "))
nums = []

for _ in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

unique_nums = []
for num in nums:
    if nums.count(num) == 1:  
        unique_nums.append(num)

print("List with only unique elements:", unique_nums)
