n=int(input())

s=str(n)
count=0
for i in range(len(s)):
    count+=int(s[i])

if n%count==0:
    print('Yes')
else:
    print('No')