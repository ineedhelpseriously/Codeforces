for _ in range(int(input())):
    x=int(input())
    b=list(map(int, input().split()))
    cn=0
    for i in b:
        if i%2!=0:
            cn+=1
    if cn%2!=0 or len(b)==1:
        print("NO")
    else:
        print("YES")