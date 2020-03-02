n,a,b=map(int,input().split())

s=pow(2,n,10**9+7)-1
x=1
for i in range(a):
    x*=(n-i)
    x%=(10**9+7)
    x*=pow(i+1,10**9+5,10**9+7)
y=1
for i in range(b):
    y*=(n-i)
    y%=(10**9+7)
    y*=pow(i+1,10**9+5,10**9+7)

print((s-x-y)%(10**9+7))