n=input().split()
k=int(n[1])
c=0
a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            c=1
            break
if c==1:
    print('YES')
else:
    print('NO')
