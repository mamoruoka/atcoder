T=int(input())
for i in range(T):
    a, s=map(int,input().split())
    #aからはbaが1のときはxyともに1, そうでないときは1,0か0,0になる
    #x,yは入れ替えても変わらない
    l = max(len(format(a, 'b')), len(format(s, 'b')))
    ba = format(a, '0'+str(l)+'b')
    bs = format(s, '0'+str(l)+'b')
    c = 0 # 繰り上げ
    ans = "Yes"
    
    for i in range(1,l+1):
        if ba[-i]=='1' and bs[-i]=='1':
            # x=1 y=1 c=1
            if c == 1:
                c = 1
            else:
                ans = "No"
                break
        elif ba[-i]=='1' and bs[-i]=='0':
            # x=1 y=1 c=0
            if c == 0:
                c = 1
            else:
                ans = "No"
                break
        elif ba[-i]=='0' and bs[-i]=='1':
            # x=0 y=0 c=1
            # x=1 y=0 c=0
            c = 0
        elif ba[-i]=='0' and bs[-i]=='0':
            # x=0 y=0 c=0
            # x=1 y=0 c=1
            if c == 1:
                c = 1
            else:
                c = 0
        
        if i==l and c == 1:
            ans = "No"
            break
            


    print(ans)
        
