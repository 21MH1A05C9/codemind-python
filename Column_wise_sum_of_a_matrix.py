n,m=map(int,input().split())
s=[0]*m
for j in range(n):
    a=list(map(int,input().split()))
    for i in range(len(a)):
        s[i]+=a[i]
for k in s:
    print(k,end=' ')