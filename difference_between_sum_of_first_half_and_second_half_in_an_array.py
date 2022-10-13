n=int(input())
a=list(map(int,input().split()))
s,s1=0,0
for i in range(0,(n//2)):
    s+=a[i]
for i in range((n//2),n):
    s1+=a[i]
print(abs(s-s1))