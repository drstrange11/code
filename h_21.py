N,K=map(int,input().split())
l=[]
l1=[]
for i in range(N):
    l=[int(l) for l in input().split()]
    l.append(l)
    if 0 in l:
        m=l.index(0)
        l1.append(m)
for i in range(len(l)):
    if 0 in l[i]:
        for j in range(K):
            l[i][j]=0
for i in l1:
    for j in range(N):
        l[j][i]=0
for i in l:
    print(*i)
