h,w=map(int,input().split())
S=[]
S.append(['0']*(w+2))
for i in range(h):
    X=['0']
    X.extend(list(input()))
    X.extend(['0'])
    S.append(X)
S.append(['0']*(w+2))    
    
for i in range(1,h+1):
    for j in range(1,w+1):
        cnt=0
        if S[i][j]=='.':
            for a in range(-1,2):
                for b in range(-1,2):
                    if a==0 and b==0: 
                        continue
                    if S[i+a][j+b]=='#':
                        cnt+=1
            S[i][j]=str(cnt)
    Y=''.join(S[i][1:w+1])
    print(Y)
