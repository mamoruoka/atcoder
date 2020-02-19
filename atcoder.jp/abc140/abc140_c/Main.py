n=int(input())
B=list(map(int,input().split()))
A=[B[0]]
for i in range(n-2):
    if B[i]<=B[i+1]:
        A.append(B[i])
    else:
        A.append(B[i+1])
A.append(B[n-2])
print(sum(A))