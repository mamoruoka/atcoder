n=int(input())
A=list(map(int,input().split()))
q=int(input())

C=[0]*(10**5+1)

for a in A:
    C[a]+=1

ans=sum(A)

for i in range(q):
    b,c=map(int,input().split())
    ans+=(c-b)*(C[b])
    C[c]+=C[b]
    C[b]=0
    print(ans)