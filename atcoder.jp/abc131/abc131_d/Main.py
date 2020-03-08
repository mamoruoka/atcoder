n=int(input())
x=[]
for _ in range(n):
    a,b=map(int,input().split())
    x.append([a,b,b-a])

x.sort(key=lambda x:(x[1],x[0]))
t=0
ans='Yes'
for i in range(n):
    if t+x[i][0]<=x[i][1]:
        t+=x[i][0]
    else:
        ans='No'
        break
print(ans)