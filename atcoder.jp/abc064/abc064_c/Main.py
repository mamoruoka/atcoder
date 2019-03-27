n=int(input())

A=list(map(int,input().split()))

C=[0]*9

for i in A:
    x=i//400
    if x<8:
        C[x]=1
    else:
        C[8]+=1
b=sum(C[:8])
print(str(max(b,1))+' '+str(b+C[8]))