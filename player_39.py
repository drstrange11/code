#AJ_39
n=int(input())
for power in range(100):
    if n==2**power:
        print("yes")
        break
else:
    print("no")
