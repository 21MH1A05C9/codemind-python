import sys 
def thirdLargest(arr,arr_size):
    if(arr_size<3):
        print(max(arr))
        return
    first=arr[0]
    for i in range(1,arr_size):
        if(arr[i]>first):
            first=arr[i]
    second=-sys.maxsize
    for i in range(0,arr_size):
        if(arr[i]>second and arr[i]<first):
            second=arr[i]
    third=-sys.maxsize
    for i in range(0,arr_size):
        if(arr[i]>third and arr[i]<second):
            third=arr[i]
    print(third)
m=int(input())
arr=list(map(int,input().split()))
n=len(arr)
thirdLargest(arr,n)