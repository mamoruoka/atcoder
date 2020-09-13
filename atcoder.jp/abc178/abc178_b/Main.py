a,b,c,d=map(int,input().split())
x=max(a*c,b*d)
y=max(a*d,b*c)
print(max(x,y))