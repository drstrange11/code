#AJ_127
s1,s2=input().split()
for i in s1:
    for j in s2:
        if(i==j):
            res=set(j)
            print(*res,end="")
