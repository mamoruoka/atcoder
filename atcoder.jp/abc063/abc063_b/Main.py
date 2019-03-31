import collections

s=input()

S=collections.Counter(s)
ans='yes'
for v in S.values():
    if v!=1:
        ans='no'
        break
print(ans)