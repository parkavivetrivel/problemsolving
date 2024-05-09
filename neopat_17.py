a = [2, 9, 8, 7, 6]
b = a[0]
a.pop(0)
a.reverse()
for i in range(0, len(a)):
    if i % b == 0 and i != 0:
        print()
    print(a[i], end=" ")
