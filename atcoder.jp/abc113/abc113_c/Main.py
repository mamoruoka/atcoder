n,m=map(int,input().split())

X=[]

for i in range(m):
    a=i
    b,c=map(int,input().split())
    X.append([a,b,c])

sort_X=sorted(X,key=lambda x:(x[1],x[2]))
sort_X[0].append(1)

for i in range(1,m):
    if sort_X[i][1]!=sort_X[i-1][1]:
        sort_X[i].append(1)
    else:
        sort_X[i].append(sort_X[i-1][3]+1)
   
X=sorted(sort_X,key=lambda x:x[0])
for i in range(m):
    count=X[i][3]
    first_num="000000"
    last_num="000000"
    
    
    first_num=first_num[:6-len(str(X[i][1]))]+str(X[i][1])
    last_num=last_num[:6-len(str(count))]+str(count)
    print(first_num+last_num)