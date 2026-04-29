n=int(input())
b=list(map(int, input().split()))
s=[]
d=[]
x=0
for _ in range(n):
    if b[0]>=b[-1]:
        x=b[0]
        b.pop(0)
    else:
        x=b[-1]
        b.pop(-1)
    if (len(s)+len(d))%2==0:
        s.append(x)
    else:
        d.append(x)
print(sum(s), sum(d))