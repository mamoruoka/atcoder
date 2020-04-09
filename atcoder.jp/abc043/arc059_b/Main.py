s=input()
ans=[-1,-1]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        ans=[i+1,i+2]
        break
    else:
        if i<=len(s)-3:
            if s[i]==s[i+2]:
                ans=[i+1,i+3]
                break
print(*ans)