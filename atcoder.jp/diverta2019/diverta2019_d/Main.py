from math import sqrt
n=int(input())
ans=0
for i in range(1,int(sqrt(n+1))):
    if n%i==0:
        ans+=n//i-1
print(ans)