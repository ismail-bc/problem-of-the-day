a = [9,4,-2,-1,5,0,-5,-3,2,9,4,8]
pos,neg,both=[],[],[]

for i in range(len(a)):
    if a[i] >= 0:
        pos.append(a[i])
    else:
        neg.append(a[i])
print(pos,"\n",neg)
    
for i in range(len(pos)):
    if len(pos) >= len(neg):
        both.append(pos[i])
        if len(neg) > i:
            both.append(neg[i])
            
    else:
        if len(pos) > i:
            both.append(pos[i])
        both.append(neg[i])
        
print(both)