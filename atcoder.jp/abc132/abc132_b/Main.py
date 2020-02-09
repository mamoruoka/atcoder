n=int(input())
p=list(map(int,input().split()))
cnt=0
for i in range(n-2):
    x=[p[i],p[i+1],p[i+2]]
    y=sorted(x)
    if x[1]==y[1]:
        cnt+=1
print(cnt)