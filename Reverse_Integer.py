n=int(input())
s=0
s1=0
if(n<0):
    m=n*(-1)
    while(m):
     s=s*10+m%10
     m=m//10
    print("-%d"%s)
else:
    while(n):
     s1=s1*10+n%10
     n=n//10
    print(s1)
        