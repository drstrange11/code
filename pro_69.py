n,k,p = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
b = list(map(int,input().split()))
b = sorted(b)
 
ans = int(2e9+1)
for i in range(k-n+1):
    tmp = 0
    for j in range(n):
        tmp = max(tmp,abs(a[j]-b[j+i])+abs(b[j+i]-p))
    ans = min(ans,tmp)
print(ans)
