n=input().lower()
n=n.replace(" ","")
c=0
for i in n:
    s=n.count(i)
    if s==1:
        c+=1
if c==0:
    print("-1")
else:
    print(c)