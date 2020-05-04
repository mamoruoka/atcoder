n=int(input())
S=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            x=str(i)+str(j)+str(k)
            p=S.find(x[0])
            q=S.find(x[1],p+1)
            r=S.find(x[2],q+1)
            if p!=-1 and q!=-1 and r!=-1:
                ans+=1
print(ans)