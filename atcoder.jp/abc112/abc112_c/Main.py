N = int(input())
xyh = [list(map(int,input().split())) for _ in range(N)]
xyh = sorted(xyh, key = lambda x: -x[2])
xt, yt, ht = xyh[0]
for Cx in range(101):
  for Cy in range(101):
    H = ht + abs(xt - Cx) + abs(yt - Cy)
    if(all(h == max(H - abs(x - Cx) - abs(y - Cy), 0) for x,y,h in xyh)):
      print(Cx, Cy, H)
      break
  else:
      continue
  break