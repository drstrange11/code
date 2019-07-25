#24
n=int(input())
n1=2**n
l1=[]
for i in range(0,n1):
    l=bin(i)[2:].zfill(n)
    if(len(l)<len(bin(2**n-1)[2:])):
        l1.append([l.count("1"),l])
    else:
        l1.append([l.count("1"),l])
l1.sort()
for i in range(len(l1)):
    print(l1[i][1])
