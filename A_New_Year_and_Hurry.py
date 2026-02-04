n,k=map(int,input().split())
timeLeft=240-k
count=0
for i in range(1,n+1):
    if timeLeft-5*i>=0:
        count+=1
        timeLeft-=5*i
    else:
        break

print(count)