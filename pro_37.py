#Pro_37
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)-1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        c+=1
    elif or l[i]<l[i-1] and l[i]<l[i+1]:
        c+=1
if len(l)==1:
    print(1)
else:
    print(c)
