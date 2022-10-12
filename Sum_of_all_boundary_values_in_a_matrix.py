a,b=map(int,input().split())
s=s1=0
for j in range(a):
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        s1+=arr[i]
        if j!=0 and j!=(a-1):
            if i!=0 and i!=len(arr)-1:
                s+=arr[i]
print(s1-s)