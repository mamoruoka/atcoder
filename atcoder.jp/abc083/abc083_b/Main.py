n,a,b=map(int,input().split())
cnt=0
for i in range(n+1):
    s=str(i)
    su=0
    for j in range(len(s)):
        su+=int(s[j])
    if su>=a and su<=b:
        cnt+=i

print(cnt)