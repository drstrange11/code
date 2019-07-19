n=int(input())
while n%10==0:
    n//=10
n=str(n)
k=n[::-1]
if n==k:
    print("yes")
else:
    print("no")
