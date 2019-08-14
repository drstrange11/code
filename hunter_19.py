#19
l=list(map(int,input().split()))
n=int(axx[0])
x=int(axx[1])
y=[]
for i in range(0,n):
    y.append(input().split())
uniq=set(y[0])
for i in y:
    uniq=uniq & set(i)
l1=list(uniq)
l1.sort()
print(*l1)
