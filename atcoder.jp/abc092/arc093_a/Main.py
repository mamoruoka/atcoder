n=int(input())
A=list(map(int,input().split()))
A=[0]+A+[0]
cnt=0
for i in range(n+1):
    cnt+=abs(A[i+1]-A[i])

for i in range(1,n+1):
    if (A[i-1]-A[i])*(A[i]-A[i+1])>=0:
        print(cnt)
    else:
        print(cnt-abs(A[i-1]-A[i])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))