b=list(map(int,input().split()))
b=sorted(b)
minn=10**5
for i in range(b[2]):
    x=abs(i-b[0])+abs(i-b[1])+abs(i-b[2])
    minn=min(x,minn)
print(minn)