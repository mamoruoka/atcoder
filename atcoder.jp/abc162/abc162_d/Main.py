n=int(input())
s=input()
L=len(s)
ans=0

r=s.count('R')
b=s.count('B')
g=s.count('G')

for i in range(L-2):
    for j in range(i+1,L-1):
        if s[j]!=s[i]:
            if j+j-i<=L-1:
                if s[j+j-i]!=s[i] and s[j+j-i]!=s[j]:
                    ans+=1
print(r*b*g-ans)