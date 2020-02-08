n,l=map(int,input().split())
x=[]
for i in range(n):
    x.append(i+l)

if max(x)*min(x)<=0:
    print(sum(x))
elif min(x)>0:
    print(sum(x)-min(x))
elif max(x)<0:
    print(sum(x)-max(x))