n,k=map(int,input().split())

s=input()
ANS=[]
cnt=0
if s[0]=='L':
    for i in range(n-1):
        if s[i]=='R' and s[i+1]=='L':
            cnt+=1
    if s[n-1]=='R':
        cnt+=1
    if cnt<=k:
        ANS.append(n-1)
    else:
        if s[n-1]=='R':
            ANS.append(n-1-1-2*(cnt-k-1))
        else:
            ANS.append(n-1-2*(cnt-k))
CNT=0
if s[0]=='R':
    for i in range(n-1):
        if s[i]=='L' and s[i+1]=='R':
            CNT+=1
    if s[n-1]=='L':
        CNT+=1
    if CNT<=k:
        ANS.append(n-1)
    else:
        if s[n-1]=='L':
            ANS.append(n-1-1-2*(CNT-k-1))
        else:
            ANS.append(n-1-2*(CNT-k))

print(max(ANS))