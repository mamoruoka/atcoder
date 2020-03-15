n,k=map(int,input().split())
r,s,p=map(int,input().split())
T=input()
cnt=0
N=[0]*n
for i in range(n):
    if N[i]==1:
        continue
    if i+k<=n-1:
        if T[i]==T[i+k]:
            N[i+k]=1
    
    if T[i]=='r':
        cnt+=p
    elif T[i]=='s':
        cnt+=r
    else:
        cnt+=s

print(cnt)