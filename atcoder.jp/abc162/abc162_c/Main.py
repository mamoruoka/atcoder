from math import gcd

ans=0
k=int(input())
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            ans+=gcd(gcd(i,j),l)
print(ans)