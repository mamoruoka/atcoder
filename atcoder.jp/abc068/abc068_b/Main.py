n=int(input())
cnt=1
X=[]
def two(n):
    cnt=0
    while n%2==0:
        n=n/2
        cnt+=1
    return cnt
res=0  
ans=n
for i in range(n,1,-1):
    if res<two(i):
        res=two(i)
        ans=i

print(ans)