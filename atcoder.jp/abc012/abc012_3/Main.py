n=int(input())

a=2025-n

X=[]

for i in range(1,10):
    for j in range(1,10):
        if i*j==a:
            X.append([i,j])

X=sorted(X,key=lambda x:(x[0],x[1]))



for p,q in X:
    print(str(p)+' x '+str(q))