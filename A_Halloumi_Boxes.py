for _ in range(int(input())):
    n,k=map(int,input().split())
    b=list(map(int, input().split()))
    if b==sorted(b):
        print("YES")
    elif len(set(b))>1 and k==1:
        print("NO")
    else:
        print("YES")