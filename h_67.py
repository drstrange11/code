n=input().split("#")
k=input().split("#")
g=["0","1","2","3","4","5","6","7","8","9"]
li=[]
l=[]
for i in n:
    for j in g:
        if j in i:
         li.append(int(i))
h=sum(li)
for i in k:
    for j in g:
        if j in i:
            l.append(int(i))
v=sum(l)
if h>v:
    print(n[0])
else:
    print(k[0])
