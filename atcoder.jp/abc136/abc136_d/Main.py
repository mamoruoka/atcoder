s=input()+'R'

n=len(s)

C=[0]*n

cnt_r=0
cnt_l=0


def calc(tmp_r,tmp_l,cnt_r,cnt_l):        
    C[tmp_r]=(cnt_r-1)//2+cnt_l//2+1
    C[tmp_l]=cnt_r//2+(cnt_l-1)//2+1

for i in range(n-1):
    if s[i]=='R' and s[i+1]=='R':
        cnt_r+=1
    
    if s[i]=='R' and s[i+1]=='L':
        cnt_r+=1
        tmp_r=i
        tmp_l=i+1
        
    if s[i]=='L' and s[i+1]=='R':
        cnt_l+=1
            
        calc(tmp_r,tmp_l,cnt_r,cnt_l)
        
        cnt_r=0
        cnt_l=0
    if s[i]=='L' and s[i+1]=='L':
        cnt_l+=1
    

        

print(*C[:-1])