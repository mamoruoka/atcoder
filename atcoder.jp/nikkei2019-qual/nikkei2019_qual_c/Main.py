n=int(input())
C=[]

for i in range(n):
    a,b=map(int,input().split())
    C.append([a+b,a,b])
    

count_a=0
count_b=0

C.sort(reverse=True)

for j in range(n):
    if(j%2==0):
        count_a+=C[j][1]
    else:
        count_b+=C[j][2]

print(count_a-count_b)