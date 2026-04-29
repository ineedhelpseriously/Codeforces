for i in range(5):
    x=list(map(int,input().split()))
    if len(set(x))>1:
        y=x.index(1)
        print(abs(2-y)+abs(2-i))