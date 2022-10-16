n=input()
a=input()
s=0
for i in range(len(n)):
    if n[i]==a:
        print(True)
        print(i)
        s=1
        break
if s!=1:
    print(False)