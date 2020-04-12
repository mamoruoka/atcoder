from collections import defaultdict

s=input()
l=len(s)
X=defaultdict(int)
i=0
ANS=set(['10','J','Q','K','A'])
flag=True
while i<=l-1 and flag:

    if s[i+1]=='J' or s[i+1]=='Q' or s[i+1]=='K' or s[i+1]=='A':
        X[s[i]]+=1
        i+=2
    elif s[i+1]=='1':
        X[s[i]]+=1
        i+=3
    else:
        i+=2
    for k,v in X.items():
        if v==5:
            end=i
            key=k
            flag=False
            break

ans=s[:end]

Y=[key+a for a in ANS]

for y in Y:
    ans=ans.replace(y,'')
if ans=='':
    print(0)
else:
    print(ans)