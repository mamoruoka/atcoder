import bisect

n, m = map(int, input().split())
x, y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
a = 0
while True:
    b = bisect.bisect_left(B, A[a] + x)
    ans += 1
    if b == m:
        break
    a = bisect.bisect_left(A, B[b] + y)
    ans += 1
    if a == n:
        break
print(ans // 2)