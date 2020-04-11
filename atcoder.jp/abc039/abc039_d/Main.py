H, W = map(int, input().split())
M = ['#' * (W + 2)]
for i in range(H):
    M.append('#' + input() + '#')
M.append('#' * (W + 2))
A = [['.'] * W for _ in range(H)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if M[i][j] == M[i - 1][j] == M[i + 1][j] == '#' and M[i][j + 1] == M[i - 1][j + 1] == M[i + 1][j + 1] == '#' and \
                M[i][j - 1] == M[i - 1][j - 1] == M[i + 1][j - 1] == '#':
            A[i - 1][j - 1] = '#'
B=[['.']*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j]=='#':
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<=H-1 and 0<=j+y<=W-1:
                        B[i+x][j+y]='#'
flag=True
for i in range(H):
    if M[i+1][1:W+1]!=''.join(B[i]):
        flag=False

if flag:
    print('possible')
    for i in range(H):
        print(''.join(A[i]))
else:
    print('impossible')