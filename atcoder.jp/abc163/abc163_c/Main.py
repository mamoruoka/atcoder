n=int(input())
A=list(map(int,input().split()))
N=[0]*n
for a in A:
    N[a-1]+=1

for i in N:
    print(i)