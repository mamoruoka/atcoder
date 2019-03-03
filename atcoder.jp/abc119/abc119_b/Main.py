n=int(input())
cnt=0
for i in range(n):
    x,u=map(str,input().split())
    if u=='JPY':
        cnt+=int(x)
    else:
        cnt+=float(x)*380000.0

print(cnt)