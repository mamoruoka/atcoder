n=int(input())

A=list(map(int,input().split()))
cnt=0
flag=True
while flag:
    for i in range(n):
        if A[i]%2!=0:
            flag=False
            break
        A[i]=A[i]/2
        cnt+=1

print(cnt//n)