#AJ_37
n=int(input())
c=0
for i in range(n):
    n1,n2=map(int,input().split())
    if n1<n2:
        count+=1
print(c,end='') 
