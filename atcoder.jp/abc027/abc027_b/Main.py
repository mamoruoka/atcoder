n=int(input())
A=list(map(int,input().split()))
if sum(A)%n!=0:
    print(-1)
else:
    x=sum(A)//n
    s=0
    ans=0
    for i in range(n):
        s+=A[i]
        if s!=(i+1)*x:
            ans+=1
    print(ans)