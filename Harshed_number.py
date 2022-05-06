a=int(input())
sum=0
k=a*1
while a:
    r=a%10
    sum=sum+r
    a=a//10
if k%sum==0:
    print('True')
else:
        print('False')