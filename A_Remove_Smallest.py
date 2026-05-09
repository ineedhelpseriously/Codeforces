for _ in range(int(input())):
    n=int(input())
    b=list(map(int, input().split()))
    c=sorted(list(set(b)))
    if len(c)==1 or abs(c[0]-c[-1])<len(c):
        print("YES")
    else:
        print("NO")