n=int(input())
A=list(map(int,input().split()))
x=[]
for i in range(n):
    x.append([A[i],i+1])
    
y=sorted(x,key=lambda x:x[0])
s=''
for i in range(n):
    s+=str(y[i][1])+' '
print(s)