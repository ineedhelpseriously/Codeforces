for _ in range(int(input())):
    a=int(input())
    count=0
    b=[]
    while a>0:
        x=divmod(a,10)
        a//=10
        if x[1]!=0:
            b.append(int(str(x[1])+count*"0"))
        count+=1
    print(len(b))
    print(*b)