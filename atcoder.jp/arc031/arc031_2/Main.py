from _collections import deque
import copy
M=[]
for i in range(10):
    x=[]
    y=input()
    for j in range(10):
        x.append(y[j])
    M.append(x)

cnt=sum([M[i].count('o') for i in range(10)])
ans='NO'

for i in range(10):
    for j in range(10):
        N=copy.deepcopy(M)
        N[i][j]='o'
        q=deque([[i,j]])
        c=0
        while len(q)!=0:
            px,py=q.popleft()
            if N[px][py]=='o':
                N[px][py]='x'
                c+=1
                for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0<=px+x<10 and 0<=py+y<10:
                        q.append([px+x,py+y])
        if c==cnt+1:
            ans='YES'

if cnt==1:
    ans='YES'

print(ans)