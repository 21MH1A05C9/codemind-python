def p(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return(False)
    else:
        return(True)
n=int(input())
r=0
if p(n):
    while(n):
        k=n%10
        r=r*10+k
        n=n//10
    if(p(r)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")