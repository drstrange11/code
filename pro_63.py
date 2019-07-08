s=input()
k=''
l=[]
for i in s:
    if i not in l:
        k+=i
        l.append(i)
    else:
        break
print(len(l))
