#AJ_16
x=int(input(""))
l=list(map(int,input().split()))[:x]
max=0
mi=0
if x==1:
    mi=1
    print(mi)
else:
    for i in range(0,len(l),1):
        k=l.count(i)
        if k==1:
            mi+=i   
            print(mi)
            break
