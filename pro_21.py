n=int(input())
l = list(map(int,input().split()))
l1 = sum(l[:len(l)//2])/len(l[:len(l)//2])
l2 = sum(l[(len(l)//2)+1:])/len(l[(len(l)//2)+1:])
if l1 == l2:
    print("yes")
else:
    print("no")
