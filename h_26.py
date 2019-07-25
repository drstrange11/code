N=int(input())
l1=list(map(int,input().split()))
l1.reverse()
l=len(l1)
for i in range(0,l):
    if(l-1!=i):
        print(l1[i],end="->")
    else:
        print(l1[i])
