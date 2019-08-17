#AJ_9    
k,s=list(map(int,input().split()))
flag=0
for i in range(k,s+1):
    if i>1:
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            flag+=1
print(flag)
