n=int(input())
H=list(map(int,input().split()))
ans='Yes'
ma=0
for i in range(1,n):
    if ma-1>H[i]:
        ans='No'
        break
    ma=max(ma,H[i])
print(ans)