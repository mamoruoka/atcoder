n=int(input())
x=[]
for i in range(n):
    key,val=map(str,input().split())
    x.append([key,-int(val),i+1])
dic_sort=sorted(x, key=lambda x:(x[0],x[1]))
for i in range(n):
    print(dic_sort[i][2])