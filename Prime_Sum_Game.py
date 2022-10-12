a,b,c,d=map(int,input().split())
p=0
for i in range(a,b+1):
    for j in range(c,d+1):
        p=i+j
        for k in range(2,p):
            if p%k==0:
                break
        else:
            break
    else:
        print("Takahashi")
        break
else:
    print("Aoki")
