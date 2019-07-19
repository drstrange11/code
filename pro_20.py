n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in l:
    if m==0:
        break
    q=m // i
    c+=q
    m=m-i*q
print(c)
