s=input()+'0'
ans=''
I=[]
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        I.append([s[i],i])
ans=I[0][0]+str(I[0][1]+1)
for j in range(1,len(I)):
    ans+=I[j][0]+str(I[j][1]-I[j-1][1])

print(ans)