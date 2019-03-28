n,t=map(int,input().split())

T=list(map(int,input().split()))
cnt=0
for i in range(n-1):
    
    if T[i+1]-T[i]<t:
        cnt+=(T[i+1]-T[i])
    else:
        cnt+=t
        
print(cnt+t)