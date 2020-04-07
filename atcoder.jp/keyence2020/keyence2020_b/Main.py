n=int(input())
X=[]
for i in range(n):
    x,l=map(int,input().split())
    X.append([x-l,l+x])

X.sort(key=lambda x:x[1])

a=X[0][0]-1
ans=0
for i in range(n):
    if X[i][0]<a:
        continue
    else:
        a=X[i][1]
        ans+=1
        
print(ans)