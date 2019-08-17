#AJ_17
def compute_gcd(n1,n2):   
    while(n2):
        n1,n2=n2,n1%n2      

    return n1

def compute_lcm(n1,n2):   
    lcm=(n1*n2)//compute_gcd(n1,n2) 
    return lcm

l=list(map(int,input().split()))  
print(compute_lcm(l[0],l[1]))
