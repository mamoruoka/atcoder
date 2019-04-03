n=int(input())
s=input()
cnt=s[1:].count('E')
res=cnt
for i in range(len(s)-1):
    if s[i]=='W' and s[i+1]=='W':
        cnt+=1
    if s[i]=='E' and s[i+1]=='E':
        cnt-=1
    
    if res>cnt:
        res=cnt
print(res)