n=int(input())
A=list(map(int,input().split()))
ans=0
c=0
for i in range(2,max(A)+1):
    cnt=0
    for a in A:
        if a%i==0:
            cnt+=1
    if cnt>=ans:
        ans=cnt
        c=i
print(c)