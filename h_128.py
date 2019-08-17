#AJ_128
s=input()
a=[]
for i in range(0,len(s)):
    for j in range(len(s)-1,i,-1):
        if(s[i]==s[j]):
            x=s[i:j+1]
            if(x==x[::-1]):
                a.append(x)
a=sorted(a)
for i in range(0,len(a)):
    print(a[i])
