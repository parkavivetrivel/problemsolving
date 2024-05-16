a = 5
b = [10,20,52,5]
c = sum(b)
d = 1
if c % 2 == 0:
    print(c)
else:
    for i in range(0, len(b)):
        d *= b[i]
    print(d)
