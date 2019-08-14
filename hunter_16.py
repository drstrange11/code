#16
m,n=map(int,input().split())
l=list(map(int,input().split()))
l.remove(n)
k=[]
for i in range(3):
    ab=abs(l[0]-n)
    r=l[0]
    for j in l:
        if abs(j-n)<ab:
            r=j
            ab=abs(j-n)
    k.append(r)
    l.remove(r)
for i in range(2):
    print(k[i],end=" ")
print(k[2]) 
