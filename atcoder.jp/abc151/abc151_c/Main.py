n,m=map(int,input().split())

N=[]

for i in range(n):
    N.append([0,0])

co=0
pe=0
for i in range(m):
    p,s=input().split()
    p=int(p)
    if s=='WA':
        N[p-1][0]+=1
    elif N[p-1][1]!=1:
        pe+=N[p-1][0]
        co+=1
        N[p-1][1]=1

print(str(co)+' '+str(pe))