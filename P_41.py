#41
m,n=input().split()
m=int(m)
n=int(n)
s=''
c=2
if m+n<=3 :
    for i in range(0,m+n):
        if i%2!=0:
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,m+n):
        if i==c:
            s=s+'0'
            if c==n:
                c=c+2
            else:
                c=c+3
        else:
            s=s+'1'
if int(s[len(s)-1])==0:
    print('-1')
elif m==1 and n==2: 
     print("011")
else:
    print(s)
