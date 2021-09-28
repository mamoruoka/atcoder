n,k=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
A.append(0)
cnt=0
ans=0
idx=0
same_num_len=1
while cnt<=k and idx<n:
    if A[idx]>A[idx+1]:
        cnt+=(A[idx]-A[idx+1])*same_num_len
        if cnt > k:
            cnt-=(A[idx]-A[idx+1])*same_num_len
            h = (k-cnt)//same_num_len
            ans+=(h*(A[idx]+A[idx]-h+1)*same_num_len)//2
            ans+=(A[idx]-h)*((k-cnt)%same_num_len)
            break
        ans+=((A[idx]-A[idx+1])*(A[idx]+A[idx+1]+1)*same_num_len)//2
    idx+=1
    same_num_len+=1

print(ans)