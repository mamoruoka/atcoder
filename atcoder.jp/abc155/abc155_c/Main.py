n=int(input())
d=dict()
for i in range(n):
    s=input()
    if s not in d.keys():
        d[s]=-1
    else:
        d[s]-=1

a=sorted(d.items(),key=lambda x:(x[1],x[0]))
for k,v in a:
    if v!=a[0][1]:
        break
    print(k)