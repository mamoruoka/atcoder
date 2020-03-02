n,m=map(int,input().split())
a=[]
for _ in range(m):
    s,c=map(int,input().split())
    a.append([s,c])

ans=-1
if n==1:
    for i in range(10):
        x=str(i)
        c=0
        for j in range(m):
            if x[a[j][0]-1] == str(a[j][1]):
                c+=1          
        if c==m:
            ans=i
            break
else:
    for i in range(10**(n-1),10**n):
        x=str(i)
        c=0
        for j in range(m):
            if x[a[j][0]-1] == str(a[j][1]):
                c+=1          
        if c==m:
            ans=i
            break
print(ans)