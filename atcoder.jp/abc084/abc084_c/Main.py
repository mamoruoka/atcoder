n=int(input())
X=[]
for i in range(n-1):
    c,s,f=map(int,input().split())
    X.append([c,s,f])


def dis(i):
    if i<n-2:
        cnt=X[i][1]+X[i][0]
        while i<n-2:
                if cnt<X[i+1][1]:
                    cnt=X[i+1][1]+X[i+1][0]
                else:
                    if cnt%X[i+1][2]!=0:
                        cnt+=X[i+1][2]-(cnt%X[i+1][2])+X[i+1][0]
                    else:
                        cnt+=X[i+1][0]
                i+=1
        return cnt
    elif i==n-2:
        return X[i][1]+X[i][0]
    elif i==n-1:
        return 0
    

for i in range(n):
    print(dis(i))