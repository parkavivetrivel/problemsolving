b = {}
while True:
    a = input()
    c = input()
    b[a] = c
    d = int(input())
    if d == 0:
        break
print(b)
for i, j in zip(b.keys(), b.values()):
    if 1000 <= int(j) <= 2999:
        e = int(j) * 5 / 100
        f = int(j) - e
        # print(f)
    elif int(j) > 5000:
        e = int(j) * 2 / 100
        f = int(j) - e
        b[i] = f
        # print(f)
print(b)
