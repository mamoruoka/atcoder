n=int(input())
s=[]
for i in range(n):
    x=input()
    y=[]
    for i in x:
        y.append(i)
    y.sort()
    s.append(''.join(y))

d=dict()

for i in range(n):
    if s[i] not in d.keys():
        d[s[i]]=1
    else:
        d[s[i]]+=1
ans=0
for v in d.values():
    ans+=v*(v-1)/2
print(int(ans))