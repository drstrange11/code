#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=11,103
n = int(input())
j=1
for i in range(n):
    for k in range(j):
        if k==j-1:
            print(1)
        else:
            print(1,end=" ")
    j+=2
