import math
x=int(input())
b=list(map(int , input().split()))
a=[0,b.count(1),b.count(2),b.count(3),b.count(4)]
a2left=0
total=0
total+=a[4]
if a[2]%2==0:
    total+=(a[2]/2)
else:
    total+=((a[2]-1)/2)
    a2left+=2
if a[3]>=a[1]:
    total+=a[3]
    if a2left>0:
        total+=1
else:
    total+=a[3]
    total+=math.ceil((a[1]-a[3]+a2left)/4)
print(int(total))
