#Lexological Permutation
n = int(input())
l = list(map(int,input().split()))
c,l = 0,[]
b = [x for x in range(1,n+1)]
for i in l:
    if i in b:
        b.remove(i)
d = 0
for i in range(0,n-1):
    p = l[i]
    for j in range(i+1,n):
        if p == l[j]:
            if p < b[d]:
                l[j] = b[d]
                c += 1
        else:
            l[i] = b[d]
            c += 1
        d += 1
print(c)
print(*l)
