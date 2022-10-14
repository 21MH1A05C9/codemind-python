s1=input().split()
s2=input().split()
c=0
for i in s1:
    if i in s2 and s2.count(i)==1 and s1.count(i)==1:
        c+=1
print(c)