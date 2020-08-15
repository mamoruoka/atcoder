s=input()
ans=0


if 'RR' in s:
    ans=2
else:
    ans=1

if not 'R' in s:
    ans=0

if s=='RRR':
    ans=3
print(ans)