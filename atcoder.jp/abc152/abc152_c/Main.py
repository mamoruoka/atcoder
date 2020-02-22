n=int(input())
P=list(map(int,input().split()))

m=P[0]
ans=1
for i in range(1,n):
    if m>P[i]:
        ans+=1
        m=P[i]
print(ans)