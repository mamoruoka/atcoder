n,m=map(int,input().split())
L=[]
R=[]
for i in range(m):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
if max(L)>min(R):
    print(0)
else:
    print(min(R)-max(L)+1)