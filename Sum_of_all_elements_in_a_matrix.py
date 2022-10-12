n,m=map(int,input().split())
s=0
for j in range(n):
    a=list(map(int,input().split()))
    for i in range(len(a)):
        s=s+a[i]
print(s)