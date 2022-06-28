i=int(input())
o=len(str(i))
t=i
s=0
while t>0:
    k=t%10
    s+=(k**o)
    t=t//10
    o=o-1
if(s==i):
    print(True)
else:
    print(False)