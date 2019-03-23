n=int(input())

A=list(map(int,input().split()))

X=list(set(A))

RES=[0]*100002

for i in A:
    RES[i-1]+=1
    RES[i]+=1
    RES[i+1]+=1

print(max(RES))