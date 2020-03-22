n=int(input())
 
A=list(map(int,input().split()))
 
X=[0]*(n+1)
 
for i in range(n):
    X[A[i]]+=1
 
ans=0

for i in range(n+1):
    if X[i]>1:
        ans+=X[i]*(X[i]-1)//2      
for i in range(n):
    if X[A[i]]==1:
        print(ans)
    elif X[A[i]]>1:
        print(ans-(X[A[i]]-1))