n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
x=[]
for i in range(m):
    b,c=map(int,input().split())
    x.append([b,c])
y=sorted(x,key=lambda x:(x[1],x[0]),reverse=True)

d=[]
cnt=0
for i in range(m):
    cnt+=y[i][0]
    d.extend([y[i][1]]*y[i][0])
    if cnt>n:
        break

for i in range(n):
    if len(d)<=i:
        break
    if d[i]>a[i]:
        a[i]=d[i]
    else:
        break
print(sum(a))