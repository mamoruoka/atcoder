X=[]
for i in range(3):
    a,b=map(int,input().split())
    X.append(a)
    X.append(b)
   
count_1=0
count_2=0
count_3=0
count_4=0
for i in range(6):
    if X[i]==1:
        count_1+=1
    if X[i]==2:
        count_2+=1
    if X[i]==3:
        count_3+=1
    if X[i]==4:
        count_4+=1
        
H=[count_1,count_2,count_3,count_4]

if set(H)=={1,3}:
    print('NO')
else:
    print('YES')