a = [1,2,3,4,5]
sums=[]
for i in a:
    sums.append(i)
z = 0
while z < len(a):
    for i in range(len(a)):
        x = a[z] + a[i]
        if x not in sums:
            sums.append(x)
    z+=1   
sums.sort()
print(sums)