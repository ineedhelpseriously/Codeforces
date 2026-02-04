import sys
n,m=map(int,sys.stdin.readline().split())
b=sorted(list(map(int,sys.stdin.readline().split())))
if m>=n:
    minn=10**5
    for i in range(m-n+1):
        minn=min(minn,b[i+n-1]-b[i])
        
else:
    minn=0
sys.stdout.write(str(minn))