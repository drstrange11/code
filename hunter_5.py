l=list(map(str,input()))
s=0
c=0
for i in range(0,len(l)-1):
    k=l[i]
    if int(k)!=0:
        for j in range(i+1,i+2):
            k=k+l[j]
            if int(k)<27 and int(k)>0: 
                s=s+1
            elif int(k)==0: 
                s=s-1
            else: 
                break
if s!=1: 
    c=s%2
print(s+c+1)
