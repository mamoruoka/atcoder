s=[0 for _ in range(26)]
t=[0 for _ in range(26)]
S=input()
T=input()

for i in range(len(S)):
    s[ord(S[i])-ord('a')]+=1
    t[ord(T[i])-ord('a')]+=1

s.sort()
t.sort()
if s==t:
    print('Yes')
else:
    print('No')