a,b,x=map(int,input().split())

left=0
right=10**9+1

while left+1!=right:
    mid=(left+right)//2
    if a*mid+b*len(str(mid))<=x:
        left=mid
    else:
        right=mid
print(left)