n,d=map(int,input().split())
M=[]
for i in range(n):
    l,r=map(int,input().split())
    M.append([l,r])
M.sort(key=lambda x:x[1])

x=-10**11
ans=0
# 効率よく壁を壊していく
for i in range(n):
    l=M[i][0]
    if x+d-1>=l:
        continue
    else:
        ans+=1
        x=M[i][1]
print(ans)

