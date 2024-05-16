a = 7
b = [23, 45, 76, 99,87,12,84]
g = []
c = {}
h = 0
for i in range(0, 100, 10):
    if i == 90:
        d = i
        e = 100
    else:
        d = i
        e = i + 9
    f = d, e
    c[f] = 0
# print(c)
for j in range(0, len(b)):
    # print(b[j])
    for key, value in c.items():
        # print(key[0], key[1])
        if key[0] < b[j] < key[1]:
            m = key[0], key[1]
            # print(True)
            c[m] += 1
for ke, va in c.items():
    h += va
n = a - h
c["Invalid"] = n

for k, v in c.items():
    if k != "Invalid":
        print("-".join(map(str, k)) + ":", str(v))
    else:
        print(str(k) + ":", str(v))
