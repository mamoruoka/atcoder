n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))
B=sorted(A,reverse=True)

for i in range(n):
    if A[i]<B[0]:
        print(B[0])
    else:
        print(B[1])