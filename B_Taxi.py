input()
b = list(map(int, input().split()))

c = [0]*5
for x in b:
    c[x] += 1

taxis = c[4]

# 3 + 1
m = min(c[3], c[1])
taxis += c[3]
c[1] -= m

# 2 + 2
taxis += c[2] // 2
c[2] %= 2

# 2 + 1 + 1
if c[2]:
    taxis += 1
    c[1] = max(0, c[1] - 2)

# 1 + 1 + 1 + 1
taxis += (c[1] + 3) // 4

print(taxis)
