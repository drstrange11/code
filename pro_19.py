n=int(input())
l=[]
for i in range(n):
    k=input()
    s=list(map(int,k.split()))
    l+=s
l.sort()
print(*l)
