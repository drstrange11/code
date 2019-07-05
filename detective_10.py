#Problem Link - https://www.guvi.in/codekata-level?level=pro&set=1,10

n = int(input())
l = list(map(int,input().split()))
s = 0
for i in range(1,len(l)):
    for x in l[:i]:
        if x<l[i]:
            s+=x
print(s)
