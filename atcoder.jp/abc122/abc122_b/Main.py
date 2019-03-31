s=input()

res=0
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        cnt=0
        for x in s[i:j]:
            if x not in ['A','G','C','T']:
                break
            cnt+=1
        if res<cnt:
            res=cnt

print(res)