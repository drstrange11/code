#https://www.guvi.in/codekata-level?level=hunter&set=8, 75
n = int(input())
l = list(map(int,input().split()))
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print(l[i+1],end=" ")
    else:
        print(-1,end=" ")
print(-1)
