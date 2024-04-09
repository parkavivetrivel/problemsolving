a = "abacaba"
d = []
e = []
c = 0
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            d.append(a[i:j + 1])
for j in range(0, len(d)):
    a = d.count(d[j])
    if a >= 2:
        e.append(d[j])
print(len(e[0]))
