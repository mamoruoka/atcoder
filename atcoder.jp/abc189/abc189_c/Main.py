n=int(input())
A=list(map(int,input().split()))

ans = 0
for l in range(n):
    mini = A[l]
    for r in range(l,n):
        if A[r] < mini:
            ans_new = A[r] * (r - l + 1)
            mini = A[r]
        else:
            ans_new = mini * (r - l + 1)
        if ans_new > ans:
            ans = ans_new
print(ans)



