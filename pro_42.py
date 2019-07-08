m,n=map(int,input().split())
s=list(map(int,input().split()))
if n==1:
    print(min(s))
elif n==2:
    print(max(s[0],s[m-1]))
else:
    print(max(s))
