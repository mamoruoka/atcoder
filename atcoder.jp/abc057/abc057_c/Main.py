n=int(input())

x=int(n**0.5)

for i in range(x,0,-1):
    if n%i==0:
        a=str(i)
        b=str(n//i)
        print(max(len(a),len(b)))
        break