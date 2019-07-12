n = int(input())
l = list(map(int,input().split()))
l = [bin(x) for x in l]
l.sort(reverse=True)
l = [int(x,2) for x in l]
for x in l:
    print(x)
