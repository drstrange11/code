n=int(input())
q=0
while 2**q < n:
    q=q+1
k = 2**q 
l = 2**(q-1)
if k == n:
    print(0)
elif n-l<=k-n:
    print(n-l)
else:
    print(k-n)
