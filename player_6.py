#AJ_6
s,k=map(str,input().split())
if len(s)!=len(k):
    print("no")
else:
    s2=[s.count(i) for i in s]
    s3=[k.count(i) for i in k]
if(s2==s3):
    print("yes")
else:
    print("no")

