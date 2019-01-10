n=int(input())



b=[[0,0,0]]
for j in range(n):
    a=[int(i) for i in input().split()]
    b.append(a)
    
    c= [x-y for (x, y) in zip(b[j+1], b[j])]
    
    if((abs(c[1])+abs(c[2])-c[0])%2!=0 or (abs(c[1])+abs(c[2])>c[0])):
        print("No")
        break
    
    if(j==n-1):
        print("Yes")