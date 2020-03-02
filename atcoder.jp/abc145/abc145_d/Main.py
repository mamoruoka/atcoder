x,y=map(int,input().split())

if (2*y-x)%3!=0 or (2*x-y)%3!=0 or 2*x-y<0 or 2*y-x<0:
    ans=0
else:
    a=(2*y-x)//3
    b=(2*x-y)//3
    n=a+b
    ans=1
    for i in range(min(a,b)):
        ans*=(n-i)
        ans%=(10**9+7)
        ans*=pow(i+1,10**9+5,10**9+7)
print(ans%(10**9+7))