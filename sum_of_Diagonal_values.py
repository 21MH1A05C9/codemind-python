a,b=map(int,input().split())
s=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in range(len(arr)):
        if i==j or i+j==len(arr)-1:
            s+=arr[j]
print(s)