n=int(input())
M=[]
N=[]
for i in range(n):
    x,y=map(int,input().split())
    M.append(x+y)
    N.append(x-y)


p=max(M)-min(M)
q=max(N)-min(N)
print(max(p,q))