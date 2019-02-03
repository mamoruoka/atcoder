n,m=map(int,input().split())

X=list(map(int,input().split()))

X.sort()

C=[]
for i in range(m-1):
    c=abs(X[i+1]-X[i])
    C.append(c)

if(n>=m):
    print(0)
else:
    C.sort()
    sum_c=0
    for j in range(len(C)-n+1):
        sum_c+=C[j]
    print(sum_c)