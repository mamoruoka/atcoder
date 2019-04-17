n=int(input())
s='123456'
S=[s]
for _ in range(6):
    for i in range(5):
        s=list(s)
        tmp=s[i]
        s[i]=s[i+1]
        s[i+1]=tmp
        S.append(''.join(s))

print(S[n%30])