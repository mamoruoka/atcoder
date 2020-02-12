n,m=map(int,input().split())
A=set(int(input()) for i in range(m))
 
x=[0]*(n+1)
x[0]=1
if 1 in A:
    x[1]=0
else:
    x[1]=1
 
for j in range(2,n+1):
    if j in A:
        x[j]=0
    else:
        x[j]=(x[j-1]+x[j-2])%(10**9+7)
        
 
print(x[n])