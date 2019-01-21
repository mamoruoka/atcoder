s=int(input())

x=[]

def collatz(n):
    if(n%2==0):
        return n/2
    else:
        return 3*n+1


count=0
if(s>4 or s==3):
    while(True):
        s=collatz(s)
        count+=1
        if(s==4):
            break


    
        

print(count+4)