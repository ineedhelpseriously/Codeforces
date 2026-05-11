n,m=map(int, input().split())
b=list(map(int, input().split()))
time=b[0]-1
for i in range(m-1):
    if b[i]>b[i+1]:
        time+=n-b[i]+b[i+1]
    else:
        time+=b[i+1]-b[i]
print(time)