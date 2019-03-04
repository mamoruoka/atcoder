n=int(input())

def hoge(x):
    if x%2==0:
        return x//(-2),0
    else:
        return x//(-2)+1,1


def base10_to_minus2(x):
    shou,amari=hoge(x)
    if shou:
        return base10_to_minus2(shou)+str(amari)
    return str(amari)

print(base10_to_minus2(n))