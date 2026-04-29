for _ in range(int(input())):
    a,*rest=map(int,input().split())
    print(sum(a<n for n in rest))