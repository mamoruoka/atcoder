n,k=map(int,input().split())
X=[0]*10**5
for _ in range(n):
    a,b=map(int,input().split())
    X[a-1]+=b
cnt=0
for i in range(10**5):
    cnt+=X[i]
    if cnt>=k:
        print(i+1)
        break