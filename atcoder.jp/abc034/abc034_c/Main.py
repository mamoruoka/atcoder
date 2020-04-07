mod=10**9+7
w,h=map(int,input().split())
w-=1
h-=1
x=min(w,h)
A=1
B=1
for i in range(x):
    A*=(w+h-i)
    B*=(i+1)
    A%=mod
    B%=mod
print((A*pow(B,mod-2,mod))%mod)