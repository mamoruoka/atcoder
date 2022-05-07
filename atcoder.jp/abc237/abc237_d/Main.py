from collections import deque
n=int(input())
S=input()
ans=deque([n])
for i in range(n)[::-1]:
  if S[i]=="L":
    ans.append(i)
  else:
    ans.appendleft(i)
print(*ans)