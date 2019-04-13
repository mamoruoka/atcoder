a,b=map(int,input().split())

x=max(a,b)
y=min(a,b)

if x!=y:
    print(x*2-1)
else:
    print(2*x)