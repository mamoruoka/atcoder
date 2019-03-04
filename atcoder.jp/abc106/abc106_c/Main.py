s=input()
k=int(input())
cnt=0
for i in range(len(s)):
    if s[i]=='1':
        cnt+=1
    else:
        break

if k>cnt:
    print(s[cnt])
else:
    print(1)