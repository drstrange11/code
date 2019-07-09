#Transform
def find(a,b,l_diff):
    for i in range(len(a)):
        if a[i]!=b[i]:
            l_diff+=1
    return l_diff
a,b = input().split()
l_diff = abs(len(b)-len(a))
#print(l_diff)
if a==b:
    print(0)
else:
    if(len(a)>len(b)):
        print(find(b,a,l_diff))
    else:
        print(find(a,b,l_diff))
