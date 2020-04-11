N = int(input())
M = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        M[i].append([x, str(y)])

ans = 0
for i in range(2 ** N):
    S = format(i, 'b').zfill(N)
    flag = True
    for j in range(N):
        if S[j] == '1':
            for x, y in M[j]:
                if S[x - 1] != y:
                    flag = False
    if flag:
        ans = max(ans, S.count('1'))
print(ans)