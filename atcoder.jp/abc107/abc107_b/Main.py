h,w=map(int,input().split())
a=['']*h
for i in range(h):
    a[i]=input()

row=[False]*h
col=[False]*w
for i in range(h):
    for j in range(w):
        if a[i][j]=='#':
            row[i]=True
            col[j]=True

for i in range(h):
    char=''
    if row[i]:
        for j in range(w):
            if col[j]:
                char+=a[i][j]
            else:
                continue
    else:
        continue
    print(char)