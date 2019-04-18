n,k=map(int,input().split())
T=[[]]
for _ in range(n):
    T.append(list(map(int,input().split())))

def dfs(q,v):
    if q==n:
        return v==0
    for i in range(k):
        if dfs(q+1,v^T[q+1][i]):
            return True
    return False

if dfs(0,0):
    print('Found')
else:
    print('Nothing')