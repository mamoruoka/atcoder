s=input()
l=len(s)
C=[0]*26
for i in s:
    C[ord(i)-97]+=1
ans=l
cnt=0
for i in range(26):
    if C[i]%2==1:
        cnt+=1
if cnt>1:
    ans=l//cnt-(not (l//cnt)%2)
print(ans)