a = input()
b = input()
c = []
e = []
for i in range(0,len(a)):
    if a[i] in b:
        d = i
        c.append(a[d:d+len(b)])
for i in range(0,len(c)):
    if sorted(c[i]) == sorted(b):
        print(c[i])
        e.append(c[i])
print(len(e))


