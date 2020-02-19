n=int(input())
H=list(map(int,input().split()))
c=0
C=[]

    

for i in range(n-1):
    if H[i]>=H[i+1]:
        c+=1
    else:
        C.append(c)
        c=0
    if i==n-2:
        C.append(c)
if len(H)!=1:        
    ans=max(C)
else:
    ans=0

print(ans)