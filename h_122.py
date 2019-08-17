#AJ_122
n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n):
    if(sum(l[:i])==sum(l[i+1:])):
        x=x+1
if x>0:
    print("yes")
else:
    print("no")
