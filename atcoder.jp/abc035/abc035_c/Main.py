n,q=map(int,input().split())


y=[]

for j in range(n+1):
    y.append(0)


for i in range(q):
    l,r=map(int,input().split())
    y[l-1]+=1
    y[r]-=1

sum=0

cha=""

for l in range(n):
    sum+=y[l]
    if(sum%2==0):
        cha+=str(0)
    else:
        cha+=str(1)
    

print(cha)