#Pro_36
n=input()
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i]>l[j] and l[j]>l[k]:
                c+=1
print(c)
