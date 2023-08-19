x,y,z = input("input 3 numbers separated by a space and i will tell you wich one is biggeer: ").split()


if x > y and x > z:
    print(f"{x} is the bigger number")
elif x < y and y > z:
    print(f"{y} is the bigger number")
else:
    print(f"{z} is the bigger number")