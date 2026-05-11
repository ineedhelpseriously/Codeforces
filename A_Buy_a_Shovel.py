price,coin=map(int , input().split())
count=1
while True:
    if (count*price-coin)%10==0 or (count*price)%10==0:
        break
    else:
        count+=1
print(count)