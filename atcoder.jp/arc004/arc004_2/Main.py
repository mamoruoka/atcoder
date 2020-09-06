n=int(input())
D=[]
for i in range(n):
    d=int(input())
    D.append(d)

x=sum(D)
y=max(D)

print(x)

if y>x-y:
    print(2*y-x)
else:
    print(0)