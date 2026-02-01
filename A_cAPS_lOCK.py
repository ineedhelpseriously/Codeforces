a=input()
b=[]
if a.isupper() or a[1:].isupper() or len(a)==1:
    for x in a:
        if x.isupper():
            b.append(x.lower())
        else:
            b.append(x.upper())
else:
    b.append(a)

print(*b,sep="")
