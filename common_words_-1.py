a=input().lower()
b=input().lower()
a=a.split(" ")
b=b.split(" ")
c=0
for i in a:
    for j in b:
       if i==j:
           c+=1
print(c)