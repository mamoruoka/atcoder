n=int(input())
X=[]
for i in range(2):
    X.append(list(map(int,input().split())))
    
res=0
for i in range(n):
    x=X[0][:i+1]
    y=X[1][i:]
    cnt=sum(x)+sum(y)
    if cnt>res:
        res=cnt

print(res)