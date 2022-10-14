s=list(map(str,input().split()))
a=b=0
for i in s:
    s1=ord(min(i))
    a+=s1
    s2=ord(max(i))
    b+=s2
    print(abs(a-b),end=' ')
    a=b=0