n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1,-1,-1):
    if a[i]%2:
        print(i)
        break
    