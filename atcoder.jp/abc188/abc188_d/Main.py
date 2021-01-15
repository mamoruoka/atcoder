N,C = map(int,input().split())
K = []
for i in range(N):
    a,b,c=map(int,input().split())
    K.append([a,c,1])
    K.append([b+1,c,-1])

K.sort(key=lambda x:(x[0],x[2]*-1))

ans=0
s=0
for i in range(2*N-1):
    if K[i][2] > 0:
        s+=K[i][1]
    else:
        s-=K[i][1]
    
    if s>C:
        ans+=C*int(K[i+1][0]-K[i][0])
    else:
        ans+=s*int(K[i+1][0]-K[i][0])


print(ans)
    



