n,m=map(int,input().split())
l=[]
for _ in range(n):
	l.append(input())
for i in range(len(l)):
	if('0' in l[i]):
		l[i]=l[i].replace('0','')
	l[i]=l[i].replace(' ','')
lengths=[]
for i in l:
	if(len(i)>0):
		lengths.append(len(i))
m=min(lengths)
final_ans='1 '*m
final_ans=final_ans.strip()
for i in range(m):
	print(final_ans)
