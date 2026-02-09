for i in range(int(input())):
    a=input()
    b=[]
    for i in range(6):
        b.append(int(a[i]))
    print("YES" if sum(b[0:3])==sum(b[3:6]) else "NO")