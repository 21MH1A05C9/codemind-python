n=int(input())
a=list(map(int,input().split()))
c=1
for i in range(0,n-3):
    if a[i+2]==a[i]+a[i+1]:
        c=0
    else:
        c=1
if c==0:
    print("yes")
else:
    print('no')