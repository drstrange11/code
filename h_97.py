#AJ_97
n,m=map(int,input().split())
k=max(n,m)
l=[]
for i in range(1,k):
    if n%i==0 and m%i==0:
        l.append(i)
if len(l)==1:
    print("yes")
else:
    print("no")
