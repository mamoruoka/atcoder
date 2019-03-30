n=int(input())

A=list(map(int,input().split()))
A.sort()

if n%2==0:
    X=[int(i) for i in range(1,n+1,2)]*2
elif n%2==1 and n>2:
    X=[int(i) for i in range(2,n+1,2)]*2+[0]
else:
    X=[0]    

X.sort()
ans=(2**(n//2))%(10**9+7)

for a,x in zip(A,X):
    if a!=x:
        ans=0
print(ans)