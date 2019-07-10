n,t=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    k=86400-i
    t-=k
    c+=1
    if t<=0:
        break  
print(c)
