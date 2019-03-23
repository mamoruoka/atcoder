import re
s=input().replace('?','.')
t=input()
ans='UNRESTORABLE'
for i in range(len(s)-len(t),-1,-1):
    if re.match(s[i:i+len(t)],t):
        s=s.replace('.','a')
        ans=s[:i]+t+s[i+len(t):]
        break
print(ans)