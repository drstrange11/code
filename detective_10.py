#Problem Link - https://www.guvi.in/codekata-level?level=pro&set=1,10

n = int(input())
l = list(map(int,input().split()))
s = 0
for x in l:
    s = s+ (x*(x+1)//2) - x
print(s)
