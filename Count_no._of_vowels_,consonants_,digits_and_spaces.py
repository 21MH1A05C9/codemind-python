n=input()
v=0
a=0
s=0
d=0
for i in range(0,len(n)):
    c=n[i]
    if(c>='a' and c<='z')or(c>='A'and c<='Z'):
        c=c.lower()
        if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
            v+=1
        else:
            a+=1
    elif(c>='0' and c<='9'):
        d+=1
    else:
        s+=1
print("Vowels: %d"%v)
print("Consonants: %d"%a)
print("Digits: %d"%d)
print("White spaces: %d"%s)
