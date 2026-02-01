s,n=map(int,input().split())
b=[]
for i in range(n):
    x=list(map(int,input().split()))
    b.append(x)

b.sort(key=lambda item:item[0])
for i in b:
        if s>i[0]:
            s+=i[1]
        else:
            print("NO")
            break
else:
        print("YES")