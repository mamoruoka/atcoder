n,s=map(str,input().split())
n=int(n)
ans=0
for i in range(n-1):
    X=[0,0,0,0]
    if s[i]=='A':
        X[0]+=1
    elif s[i]=='G':
        X[1]+=1
    elif s[i]=='C':
        X[2]+=1
    else:
        X[3]+=1
    for j in range(i+1,n):
        if s[j] == 'A':
            X[0] += 1
        elif s[j] == 'G':
            X[1] += 1
        elif s[j] == 'C':
            X[2] += 1
        else:
            X[3] += 1
        if X[0]==X[3] and X[1]==X[2]:
            ans+=1
print(ans)






