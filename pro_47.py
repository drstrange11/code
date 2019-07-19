#AJ divisibility
s=input().split()
g=int(s[1])
m=int(s[0])
s=[int(d) for d in s[0]]
h=0
c=1;
while(h==0):
	prod=c*m
	k=[ int(d) for d in str(prod)]
	r=0
	j=len(k)-1
	while(k[j]==0):
		r+=1
		j-=1
	if(r>=g):
		print(prod)
		h=1
	c+=1
