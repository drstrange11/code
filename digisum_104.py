#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=11 -104


n = int(input())
l = list(int(x) for x in str(n))
s = 0
for x in l:
    s = s+ (x*(x+1)//2)
print(s)
