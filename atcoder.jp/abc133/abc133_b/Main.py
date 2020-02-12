import math
n,d=map(int,input().split())
X=[]
for i in range(n):
    x=list(map(int,input().split()))
    X.append(x)
cnt=0
for i in range(n):
    for j in range(i+1,n):
        s=0
        for a,b in zip(X[i],X[j]):
            s+=(a-b)**2
        s=math.sqrt(s)
        if s.is_integer():
            cnt+=1
print(cnt)