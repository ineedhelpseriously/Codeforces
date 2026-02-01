a,b,c=input(),input(),input()
def x(a,b,c):
    for i in c:
        if c.count(i)==a.count(i)+b.count(i) and len(c)==len(a+b):
            pass
        else:
            return("NO")
    return("YES")

print(x(a,b,c))