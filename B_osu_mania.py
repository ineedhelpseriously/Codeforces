for _ in range(int(input())):
    i=int(input())
    b=[]
    for _ in range(i):
        x=input()
        if x[0]=="#":
            b.append(1)
        elif x[1]=="#":
            b.append(2)
        elif x[2]=="#":
            b.append(3)
        elif x[3]=="#":
            b.append(4)
    b.reverse()
    print(*b)