n=int(input())

a = [int(i) for i in input().split()] 

A=0
B=0

a.sort(reverse=True)

for j in range(n):
    if(j%2==0):
        A+=a[j]
    else:
        B+=a[j]
        
print(A-B)