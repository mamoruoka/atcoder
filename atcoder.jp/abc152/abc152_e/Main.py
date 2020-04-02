from fractions import gcd

def lcm(a,b):
    return a*(b//gcd(a,b))

mod=10**9+7

n=int(input())
A=list(map(int,input().split()))

L=A[0]
for i in range(1,n):
    L=lcm(L,A[i])
ans=0
for i in range(n):
    ans+=(L*pow(A[i],mod-2,mod))%mod
print(ans%mod)