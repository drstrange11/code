n,k = map(int,input().split())
l = list(map(int,input().split()))
for i in range(len(l)):
    if k-l[i] in l[i+1:]:
        print("yes")
        break
if i==len(l)-1:
    print("no")
