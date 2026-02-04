input()
b=list(map(int,input().split()))
mina=b[0]
maxa=b[0]
count=0
for i in b:
    if mina<i:
        count+=1
        mina=i
    elif maxa>i:
        count+=1
        maxa=i

print(count)