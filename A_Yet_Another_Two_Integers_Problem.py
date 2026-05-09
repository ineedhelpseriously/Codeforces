for _ in range(int(input())):
    a,b=map(int,input().split())
    x=abs(a-b)
    count=0
    if x%10==0:
        print(x//10)
    else:
        print(x//10+1)