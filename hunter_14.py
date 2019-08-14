#14
from itertools import permutations
n=input()
q=permutations(n)
l=[]
for i in list(q):
    s="".join(i)
    if s not in l:
        l.append(s)
for i in l:
    print(i)
