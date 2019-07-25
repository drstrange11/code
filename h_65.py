n,k=input().split()
n=int(n)
k=int(k)
array=list(map(int,input().split()))
l=[]
for i in range(0,n):
    if(array[i]!=k):
        l.append(array[i])
if len(l)==0:
    print("empty")
else:
    n=len(l)
    for i in range(0,n):
        if (i==(n-1)):
            print(l[i])
        else:
            print(l[i],end=" ")
