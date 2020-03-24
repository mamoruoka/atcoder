n,h=map(int,input().split())
X=[]
for i in range(n):
    a,b=map(int,input().split())
    X.append([a,b])
    
X.sort(key=lambda x:x[0],reverse=True)

Y=X[1:]
Y.sort(key=lambda x:x[1],reverse=True)

cnt=0

for i in range(n-1):
    if Y[i][1]>=X[0][1]:
        h-=Y[i][1]
        cnt+=1
        if h<=0:
            break

if h>0:
    h-=X[0][1]
    cnt+=1
    if h>0:
        for i in range(n-1):
            if Y[i][1]<X[0][1] and Y[i][1]>=X[0][0]:
                h-=Y[i][1]
                cnt+=1
                if h<=0:
                    break
        if h>0:
            if h%X[0][0]!=0:
                cnt+=h//X[0][0]+1
            else:
                cnt+=h//X[0][0]
print(cnt)