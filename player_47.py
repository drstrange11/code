#AJ_47
a1,a2,a3=map(int,input().split(" "))
if a1!=0 and a2!=0 and a3!=0:
    a=a1+a2+a3
else:
    a=0
if a==180:
    print("yes")
else:
    print("no")
