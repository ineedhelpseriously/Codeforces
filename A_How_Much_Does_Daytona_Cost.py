for _ in range(int(input())):
    x,y=map(int, input().split())
    b=list(map(int, input().split()))
    if y in b:
        print("YES")
    else:
        print("NO")