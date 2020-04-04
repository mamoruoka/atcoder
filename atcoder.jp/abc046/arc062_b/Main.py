s=input()

cnt=0
ans=0
for i in range(len(s)):
    if s[i]=='g':
        if cnt>0:
            ans+=1
            cnt-=1
        elif cnt==0:
            cnt+=1
    else:
        if cnt==0:
            ans-=1
            cnt+=1
        else:
            cnt-=1
print(ans)