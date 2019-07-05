#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=11,108
n = input()
l = list(int(x) for x in n)
s =0
for i in range(len(l)-1):
    s = s+ l[i]**l[i+1]
s = s+l[len(l)-1]**l[0]
print(s)
