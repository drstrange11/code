s=input()
b="dhoni"
f=0
if len(s) != len(b):
    print("no")
else:
    for i in b:
        if i in s:
            f=1
        else:
            f=0
            break
    if(f==1):
        print("yes")
    else:
        print("no")
