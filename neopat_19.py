a = 9
b = [4, 2, 3, 7, 8, 4, 1, 2, 3]
c = 4
d = []
b = sorted(b, reverse=True)
for i in b:
    d.append(i * c)
print(" ".join(map(str, d)))
