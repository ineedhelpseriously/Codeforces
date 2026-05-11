n,l=map(int,input().split())
b=(list(map(int,input().split())))
b=sorted(b)
dim=0
for i in range(n-1):
    dim=max(dim,b[i+1]-b[i])
if 0 not in b:
    dim=max(dim, 2*(b[0]))
if l not in b:
    dim=max(dim, 2*(l-b[-1]))
print(dim/2)