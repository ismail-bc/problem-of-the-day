from numpy import random

print("""Enter two numbers A and B separted by a space,
where A is smaller than B\nandthey mustbe between 1 and 10
and I will tell you if A and B are in a random genetated array: """)

A,B = input("hi: ").split()
A,B = int(A),int(B)
arr = list(random.randint(1,10,10))
print(arr)
if A and B in arr[A:B]:
    print("yes")
else:
    print("no")