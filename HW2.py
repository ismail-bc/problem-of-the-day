import numpy as np

x = list(input())
for i in x:
    if i == " ":
        x.remove(" ")
    
j = 9
a = 0
while a != j:
    q,w = np.random.choice(x, size=(2))
    a = int(q) + int(w)

print(q,"+", w,f"= {j}")