import collections

n=int(input())


X=list(map(int,input().split()))
odd=[]
even=[]
for i in range(int(n/2)):
    odd.append(X[2*i+1])
    even.append(X[2*i])

odd_counter=collections.Counter(odd) #登場回数とその値の辞書型
even_counter=collections.Counter(even)

odd_count=sorted(odd_counter.values(),reverse=True) #登場回数の多い順に並べた配列
even_count=sorted(even_counter.values(),reverse=True)

max_odd_value=max(odd_counter,key=odd_counter.get) #登場回数が最大の値
max_even_value=max(even_counter,key=even_counter.get)

if max_odd_value!=max_even_value:
    print(n-odd_count[0]-even_count[0])
elif len(set(odd))!=1 and len(set(even))!=1:
    print(min(n-odd_count[0]-even_count[1],n-odd_count[1]-even_count[0]))
elif len(set(odd))==1 and len(set(even))==1:
    print(int(n/2))
elif len(set(odd))==1:
    print(int(n/2)-even_count[1])
elif len(set(even))==1:
    print(int(n/2)-odd_count[1])