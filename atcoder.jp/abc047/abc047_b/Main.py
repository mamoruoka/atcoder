w,h,n=map(int,input().split())
X=[]
for i in range(n):
    x,y,a=map(int,input().split())
    X.append([x,y,a])

X_max=[0]
X_min=[w]
Y_max=[0]
Y_min=[h]


for i in range(n):
    if X[i][2]==1:
        X_max.append(X[i][0])
    elif X[i][2]==2:
        X_min.append(X[i][0])
    elif X[i][2]==3:
        Y_max.append(X[i][1])
    elif X[i][2]==4:
        Y_min.append(X[i][1])

a=min(X_min)-max(X_max)
b=min(Y_min)-max(Y_max)

if a<=0 or b<=0:
    ans=0
else:
    ans=a*b


print(ans)
        