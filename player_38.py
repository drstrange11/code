#AJ_38
n=int(input())
l1=[]
for i in range(2,n+1):
    if n%i==0:
        l1.append(i)
for n in l1:
    if n%2==0:
        print(n,end=" ")
