global second
a = "ikkkkkkkkkkbgh"
global e
global first
b = 3
c = 0
d = []
for i in range(0,len(a)):
    first = i
    d.append(a[first])
    for j in range(i,len(a)):
        if a[j] not in d:
            d.append(a[j])
            e = len(d)
    if e == b:
        print(a[first:len(a)])
        break
    else:
        d.clear()