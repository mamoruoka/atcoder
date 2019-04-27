n=int(input())
A=list(map(int,input().split()))

S=0
for a in A:
    S+=abs(a)




cnt=0
for a in A:
    if a<0:
        cnt+=1
if cnt%2==0:
    print(S)
else:
    m=abs(A[0])
    for i in range(n):
        if m>abs(A[i]):
            m=abs(A[i])
    print(S-2*m)
    