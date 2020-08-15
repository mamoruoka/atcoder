x,k,d=map(int,input().split())
if x==0:
    if k%2==0:
        ans=0
    else:
        ans=d
else:
    if x<0:
        x=-x

    if x-k*d>=x%d:
        ans=x-k*d
    else:
        y=x//d
        if (k-y)%2==0:
            ans=x-d*y
        else:
            ans=abs(x-d*(y+1))


print(ans)