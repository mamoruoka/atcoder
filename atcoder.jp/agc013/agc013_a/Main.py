n=int(input())

x=[int(i)for i in input().split()]


count=1

state=0

for i in range(1,n):
    a=state
    d=x[i]-x[i-1]
    if(d>0):
        state=1
    elif(d==0):
        pass
    elif(d<0):
        state=-1
    if(state*a==-1):
        count+=1
        state=0

    


print(count)