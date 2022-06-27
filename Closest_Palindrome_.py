def p(n):
    if str(n)[::-1]==str(n):
        return 1
    else:
        return 0
n=int(input())
for i in range(n-1,1,-1):
    if p(i):
        k=i
        break
for i in range(n+1,99999):
    if p(i):
        l=i
        break
if n-k>=l-n:
    print(k,l)
else:
    print(k)