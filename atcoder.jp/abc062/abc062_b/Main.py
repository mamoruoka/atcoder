h,w=map(int,input().split())

X=['#'*(w+2)]
for i in range(h):
    s=input()
    Y='#'+s+'#'
    X.append(Y)
X.append('#'*(w+2))

for i in range(h+2):
    print(X[i])