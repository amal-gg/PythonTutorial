A = set()
n1 = int(input("Enter number of elements in Set A: "))
for _ in range(n1):
    A.add(int(input("Enter element: ")))

B = set()
n2 = int(input("Enter number of elements in Set B: "))
for _ in range(n2):
    B.add(int(input("Enter element: ")))

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference:", A ^ B)
