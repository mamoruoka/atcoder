n=int(input())
X=[[0,0,0]]
for i in range(n):
    t,x,y=map(int,input().split())
    X.append([t,x,y])
ans='Yes'
for i in range(n):
    if (X[i+1][0]-X[i][0]-abs(X[i+1][1]-X[i][1])+abs(X[i+1][2]-X[i][2]))%2==1 or (X[i+1][0]-X[i][0]-abs(X[i+1][1]-X[i][1])-abs(X[i+1][2]-X[i][2]))<0:
        ans='No'
print(ans)
        