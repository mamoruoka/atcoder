x=int(input())

if x%11>6:
    print(2*(x//11)+2)
elif 0<x%11<=6:
    print(2*(x//11)+1)
else:
    print(2*(x//11))