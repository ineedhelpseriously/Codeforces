for _ in range(int(input())):
    x=str(bin(int(input())))
    count=0
    for i in x:
        if i=="1":
            count+=1
    if count==1:
        print("NO")
    else:
        print("YES")