n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    if l[i]==i:
        k.append(str(l[i]))
k.sort()
if len(k)==0:
    print("-1")
else:
    print(" ".join(k))
