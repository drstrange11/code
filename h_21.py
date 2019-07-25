N,K=map(int,input().split())
xx=[]
l1=[]
for i in range(N):
    l=[int(xx) for xx in input().split()]
    xx.append(l)
    if 0 in l:
        m=l.index(0)
        l1.append(m)
for i in range(len(xx)):
    if 0 in xx[i]:
        for j in range(K):
            xx[i][j]=0
for i in l1:
    for j in range(N):
        xx[j][i]=0
for i in xx:
    print(*i)
