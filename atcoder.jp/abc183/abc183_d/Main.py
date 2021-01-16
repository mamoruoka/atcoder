n,w=map(int,input().split())
X=[]
for i in range(n):
    s,t,p=map(int,input().split())
    X.append([s,p])
    X.append([t,-p])

ans='Yes'

X.sort(key=lambda x:(x[0],x[1]))
s=0

for i in range(n*2):
    s+=X[i][1]
    if s>w:
        ans='No'
        break
print(ans)