n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1):
        if (j==i) or (i==n+1-j):
            print('x',end='')
        else:
            print('0',end='')
    print()