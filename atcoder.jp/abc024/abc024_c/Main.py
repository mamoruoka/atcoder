n,d,k=map(int,input().split())
D=[]
for i in range(d):
    l,r=map(int,input().split())
    D.append([l,r])

for i in range(k):
    s,t=map(int,input().split())
    for j in range(d):
        l=D[j][0]
        r=D[j][1]
        if l<=s and s<=r:
            if s>t:
                s=max(l,t)
            else:
                s=min(r,t)
        if s==t:
            print(j+1)
            break