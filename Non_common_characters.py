a=input()
b=input()
a=a.lower()
b=b.lower()
a=set(a)
b=set(b)
c=0
for i in a:
    if i!=' ':
        if i not in b:
            c+=1
for i in b:
    if i!=" ":
          if i not in a:
            c+=1
print(c)