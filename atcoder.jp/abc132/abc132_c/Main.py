n=int(input())
d=list(map(int,input().split()))
d.sort()
x=len(d)
if x%2==1:
    print(0)
else:
    print(d[x//2]-d[x//2-1])