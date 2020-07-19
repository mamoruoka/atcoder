from itertools import product
h,w,k=map(int,input().split())
M=[input() for i in range(h)]
a=0
for A in product([0,1],repeat=h):
    for B in product([0,1],repeat=w):
        ANS=0
        for i in range(h):
            for j in range(w):
                if M[i][j]=='#' and A[i]==0 and B[j]==0:
                    ANS+=1
        if ANS==k:
            a+=1

print(a)
