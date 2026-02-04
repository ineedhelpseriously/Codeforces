input()
b=list(map(int,input().split()))
x=[0]
for i in b:
    if i==-1 and x[-1] in [0, -1]:
        x.append(i)
    elif i>0 and x[-1] in [0,-1]:
        x.append(i)
    elif i>0 and x[-1]>0:
        x[-1]+=i
    elif i==-1 and x[-1]>0:
        x[-1]-=1
print(x.count(-1))
