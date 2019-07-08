#Pro_32
a,b=map(int,input().split())
if a>b:
    a,b=b,a
l=[]
for i in range(a):
    m=list(map(int,input().split()))
    m.sort()
    l.append(m)
for j in range(0,b):
    n=[]
    for i in range(0,a):
        n.append(l[i][j])
    n.sort()
    r=0
    for i in range(0,a):
        l[i][j]=n[r]
        r=r+1
for i in l:
    print(*i)
