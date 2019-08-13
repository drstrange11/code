#69
n,k,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
l=[]
for i in range(n):
    l.append(m-q[i])
    l.append(abs(w[i]-q[i]) +(w[i]-m))
print(max(l))
