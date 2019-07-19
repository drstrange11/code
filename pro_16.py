n = int(input())
l = list(map(int,input().split()))
k = [1]*n
for i in range(n):
    if i == 0 and l[i] > l[i+1]:
        k[i] += k[i+1]
    if i > 0 and l[i] > l[i-1]:
        k[i] += k[i-1]
print(sum(k))
