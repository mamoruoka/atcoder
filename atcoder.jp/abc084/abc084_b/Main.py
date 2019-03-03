a,b=map(int,input().split())
s=input()
ans='No'
cnt=0
if s[a]=='-':
    s=s[:a]+s[a+1:]
    if '-' not in s:
        ans='Yes'

print(ans)