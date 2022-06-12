from collections import defaultdict
n=int(input())
A=list(map(int,input().split()))
ans=(n*(n-1)*(n-2))//6
X=defaultdict(int)
for a in A:
    X[a]+=1
X=dict(X)
s=0
for x in X.values():
    s+=x
for x in X.values():
    if x==2:
        ans-=s-x
    elif x>2:
        ans-=(s-x)*(x*(x-1)/2)
        ans-=x*(x-1)*(x-2)/6
print(int(ans))
