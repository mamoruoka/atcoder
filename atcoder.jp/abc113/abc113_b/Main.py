n=int(input())

t,a=map(int,input().split())

H=list(map(int,input().split()))
    
new_h=[abs(t-H[i]*0.006-a) for i in range(n)]

print(new_h.index(min(new_h))+1)