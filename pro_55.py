from itertools import combinations

n,k = map(int,input().split())
l = list(map(int,input().split()))
new = []
s = []
for x in l:
    new = new+[x]*k 
for x in list(combinations(new,k)):
    s.append(sum(x))
s = sorted(list(set(s)))
print(*s)
