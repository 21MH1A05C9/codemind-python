s=list(map(str,input().split()))
l=len(s)
s=s[l-1]
a=min(s)
b=a.lower()
for i in s:
    if s.count(b)!=0:
        print(b)
        break
    else:
        print(a)
        break