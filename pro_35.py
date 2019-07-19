#k dominant
c=input()
l=list(set(c))
x=1
ant=0
check=False
while True:
    ch=l[ant]
    for y in range(0,len(c)-x):
        if ch in c[y:y+x]:
            check=True
        else:
            check=False
            ant=ant+1
            if ant>=len(l):
                ant=0
                x+=1
            break

    if check==True:
        break
print(x)
